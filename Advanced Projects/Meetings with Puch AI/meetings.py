import asyncio
import os
from pathlib import Path
from typing import Annotated, Optional
import datetime
import uuid

from fastmcp import FastMCP
from fastmcp.server.auth.providers.bearer import BearerAuthProvider, RSAKeyPair
from mcp import ErrorData, McpError
from mcp.server.auth.provider import AccessToken
from mcp.types import INTERNAL_ERROR, INVALID_PARAMS, TextContent
from pydantic import Field, BaseModel

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- CONFIGURATION ---
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("PUCH_TOKEN")
if not TOKEN:
    raise ValueError("PUCH_TOKEN environment variable not set.")

MY_NUMBER = os.getenv("MY_PHONE_NUMBER")
if not MY_NUMBER:
    raise ValueError("MY_PHONE_NUMBER environment variable not set.")

SCOPES = ['https://www.googleapis.com/auth/calendar']


class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None


class SimpleBearerAuthProvider(BearerAuthProvider):
    def __init__(self, token: str):
        k = RSAKeyPair.generate()
        super().__init__(
            public_key=k.public_key, jwks_uri=None, issuer=None, audience=None
        )
        self.token = token

    async def load_access_token(self, token: str) -> AccessToken | None:
        if token == self.token:
            return AccessToken(
                token=token,
                client_id="puch-client",
                scopes=["*"],
                expires_at=None,
            )
        return None


# --- MCP Server Setup ---
mcp = FastMCP(
    "Google Calendar MCP Server",
    auth=SimpleBearerAuthProvider(TOKEN),
)

# --- Google Calendar API Service ---
def get_calendar_service():
    """Creates and returns a Google Calendar API service object."""
    creds = None
    token_path = Path(__file__).parent / 'token.json'
    credentials_path = Path(__file__).parent / 'credentials.json'

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_path.exists():
                raise FileNotFoundError(
                    "FATAL: 'credentials.json' not found. Please follow the setup instructions."
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

# --- Internal Helper Functions ---

async def _find_events_by_query(query: str) -> list[dict]:
    """Internal helper to find events based on a text query."""
    service = get_calendar_service()
    if not service:
        return []

    now = datetime.datetime.now(datetime.UTC)
    # Search for events in the next 30 days
    time_max = now + datetime.timedelta(days=30)
    
    try:
        events_result = service.events().list(
            calendarId='primary', 
            timeMin=now.isoformat(),
            timeMax=time_max.isoformat(),
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        all_events = events_result.get('items', [])
        
        # Filter events where the query matches the summary (case-insensitive)
        matching_events = [
            event for event in all_events 
            if query.lower() in event.get('summary', '').lower()
        ]
        return matching_events
    except HttpError as error:
        print(f"An error occurred while searching for events: {error}")
        return []


# --- MCP Tools for Google Calendar ---

# Tool: Create Event
CreateEventToolDescription = RichToolDescription(
    description="Creates a new event on your Google Calendar.",
    use_when="When you want to schedule a new event, meeting, or reminder.",
    side_effects="A new event will be added to your primary Google Calendar."
)

@mcp.tool(description=CreateEventToolDescription.model_dump_json())
async def create_calendar_event(
    summary: Annotated[str, Field(description="The title or summary of the event.")],
    start_time: Annotated[str, Field(description="The start time of the event in ISO 8601 format (e.g., '2025-12-31T10:00:00').")],
    end_time: Annotated[str, Field(description="The end time of the event in ISO 8601 format (e.g., '2025-12-31T11:00:00').")],
    location: Annotated[Optional[str], Field(description="The location of the event.")] = None,
    description: Annotated[Optional[str], Field(description="A description of the event.")] = None
) -> str:
    """Creates a new event on the user's primary calendar."""
    service = get_calendar_service()
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
    }
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        return f"Event created: '{summary}'. View it here: {event.get('htmlLink')}"
    except HttpError as error:
        return f"An error occurred: {error}"

# Tool: Read Events (Upgraded)
ReadEventsToolDescription = RichToolDescription(
    description="Lists upcoming events from your Google Calendar, including their IDs.",
    use_when="When you want to know what's on your schedule or check for upcoming events.",
    side_effects="None. This tool only reads data from your calendar."
)

@mcp.tool(description=ReadEventsToolDescription.model_dump_json())
async def read_calendar_events(
    max_results: Annotated[int, Field(description="The maximum number of events to return.", default=10)]
) -> str:
    """Lists the next upcoming events and their IDs from the user's primary calendar."""
    service = get_calendar_service()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    try:
        events_result = service.events().list(
            calendarId='primary', timeMin=now,
            maxResults=max_results, singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        if not events:
            return "No upcoming events found."

        # Format the output to be more structured and include the ID
        event_list = "Upcoming Events:\n"
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list += (
                f"\n- Summary: {event.get('summary', 'No Title')}\n"
                f"  Time: {start}\n"
                f"  ID: {event['id']}\n"
            )
        return event_list
    except HttpError as error:
        return f"An error occurred: {error}"

# Tool: Find Event (New and Smart)
FindEventToolDescription = RichToolDescription(
    description="Finds a specific calendar event by its name or title.",
    use_when="When you need to find the details or ID of a specific event before updating or deleting it.",
    side_effects="None. This tool only reads data from your calendar."
)

@mcp.tool(description=FindEventToolDescription.model_dump_json())
async def find_calendar_event(
    query: Annotated[str, Field(description="The name, title, or keyword of the event to find (e.g., 'Project Sync' or 'Dentist').")]
) -> str:
    """Finds a calendar event by searching for a query in the event summary."""
    matching_events = await _find_events_by_query(query)
    
    if not matching_events:
        return f"No events found matching '{query}' in the next 30 days."
    
    if len(matching_events) > 1:
        response = f"Found multiple events matching '{query}'. Please use the specific ID to update or delete:\n"
        for event in matching_events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            response += (
                f"\n- Summary: {event.get('summary', 'No Title')}\n"
                f"  Time: {start}\n"
                f"  ID: {event['id']}\n"
            )
        return response

    event = matching_events[0]
    start = event['start'].get('dateTime', event['start'].get('date'))
    return (
        "Found one event:\n"
        f"- Summary: {event.get('summary', 'No Title')}\n"
        f"- Time: {start}\n"
        f"- Location: {event.get('location', 'Not specified')}\n"
        f"- Description: {event.get('description', 'Not specified')}\n"
        f"- ID: {event['id']}"
    )

# Tool: Delete Event (Upgraded)
DeleteEventToolDescription = RichToolDescription(
    description="Deletes an event from your Google Calendar by its name.",
    use_when="When you want to cancel or remove an event. e.g., 'delete my project sync meeting'.",
    side_effects="The specified event will be permanently removed from your primary Google Calendar if only one match is found."
)

@mcp.tool(description=DeleteEventToolDescription.model_dump_json())
async def delete_calendar_event(
    query: Annotated[str, Field(description="The name, title, or keyword of the event to delete (e.g., 'Project Sync' or 'Dentist').")]
) -> str:
    """Deletes an event from the user's primary calendar by searching for its name."""
    matching_events = await _find_events_by_query(query)
    
    if not matching_events:
        return f"Could not find any event matching '{query}' to delete."

    if len(matching_events) > 1:
        response = f"Found multiple events matching '{query}'. Please be more specific or use the 'find_calendar_event' tool to get a specific ID.\n"
        for event in matching_events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            response += f"\n- Summary: {event.get('summary', 'No Title')}, Time: {start}, ID: {event['id']}"
        return response

    event_to_delete = matching_events[0]
    event_id = event_to_delete['id']
    event_summary = event_to_delete.get('summary', 'No Title')

    try:
        service = get_calendar_service()
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return f"Successfully deleted the event: '{event_summary}'."
    except HttpError as error:
        return f"An error occurred while trying to delete the event: {error}"

# Tool: Update Event (Upgraded)
UpdateEventToolDescription = RichToolDescription(
    description="Updates an event on your Google Calendar by finding it with a query.",
    use_when="When you need to change an event's details. e.g., 'update my project sync meeting'.",
    side_effects="The specified event will be modified on your calendar if only one match is found."
)

@mcp.tool(description=UpdateEventToolDescription.model_dump_json())
async def update_calendar_event(
    query: Annotated[str, Field(description="The name or title of the event to update.")],
    new_summary: Annotated[Optional[str], Field(description="The new title for the event.")] = None,
    new_start_time: Annotated[Optional[str], Field(description="The new start time in ISO 8601 format.")] = None,
    new_end_time: Annotated[Optional[str], Field(description="The new end time in ISO 8601 format.")] = None,
    new_location: Annotated[Optional[str], Field(description="The new location for the event.")] = None,
    new_description: Annotated[Optional[str], Field(description="The new description for the event.")] = None
) -> str:
    """Updates an existing event by searching for it by name and applying the changes."""
    matching_events = await _find_events_by_query(query)

    if not matching_events:
        return f"Could not find any event matching '{query}' to update."

    if len(matching_events) > 1:
        response = f"Found multiple events matching '{query}'. Please be more specific or use the 'find_calendar_event' tool to get a specific ID.\n"
        for event in matching_events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            response += f"\n- Summary: {event.get('summary', 'No Title')}, Time: {start}, ID: {event['id']}"
        return response

    event_to_update = matching_events[0]
    event_id = event_to_update['id']
    
    try:
        service = get_calendar_service()
        # Get the latest version of the event before updating
        event = service.events().get(calendarId='primary', eventId=event_id).execute()

        # Update fields only if new values are provided
        if new_summary: event['summary'] = new_summary
        if new_location: event['location'] = new_location
        if new_description: event['description'] = new_description
        if new_start_time: event['start']['dateTime'] = new_start_time
        if new_end_time: event['end']['dateTime'] = new_end_time

        updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
        return f"Event '{updated_event.get('summary')}' updated successfully. View it here: {updated_event.get('htmlLink')}"
    except HttpError as error:
        return f"An error occurred while trying to update the event: {error}"


@mcp.tool
async def validate() -> str:
    """NOTE: This tool must be present in an MCP server used by puch for validation."""
    return MY_NUMBER


async def main():
    print("Starting MCP server on http://0.0.0.0:8085")
    print("Make sure to use a tool like ngrok to make it publicly accessible.")
    await mcp.run_async("streamable-http", host="0.0.0.0", port=8085)


if __name__ == "__main__":
    asyncio.run(main())
