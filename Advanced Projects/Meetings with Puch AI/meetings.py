import asyncio
import os
from pathlib import Path
from typing import Annotated, Optional
import datetime

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
# 1. Get the application key from environment variables (e.g., in a .env file)
# Create a .env file and add PUCH_TOKEN="your_secret_token"
# and MY_PHONE_NUMBER="your_phone_number"
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("PUCH_TOKEN")
if not TOKEN:
    raise ValueError("PUCH_TOKEN environment variable not set.")

MY_NUMBER = os.getenv("MY_PHONE_NUMBER")
if not MY_NUMBER:
    raise ValueError("MY_PHONE_NUMBER environment variable not set.")

# 2. If modifying these SCOPES, delete the file token.json.
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
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

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
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',  # Change to your timezone
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',  # Change to your timezone
        },
    }
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        return f"Event created successfully. View it here: {event.get('htmlLink')}"
    except HttpError as error:
        return f"An error occurred: {error}"

# Tool: Read Events
ReadEventsToolDescription = RichToolDescription(
    description="Lists upcoming events from your Google Calendar.",
    use_when="When you want to know what's on your schedule or check for upcoming events.",
    side_effects="None. This tool only reads data from your calendar."
)

@mcp.tool(description=ReadEventsToolDescription.model_dump_json())
async def read_calendar_events(
    max_results: Annotated[int, Field(description="The maximum number of events to return.", default=10)]
) -> str:
    """Lists the next upcoming events from the user's primary calendar."""
    return await _read_calendar_events_logic(max_results)

async def _read_calendar_events_logic(max_results: int = 10) -> str:
    """This is the core logic for reading calendar events."""
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    try:
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=max_results, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            return "No upcoming events found."

        event_list = ""
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list += f"- {start}: {event['summary']}\n"
        return event_list
    except HttpError as error:
        return f"An error occurred: {error}"

# Tool: Update Event
UpdateEventToolDescription = RichToolDescription(
    description="Updates an existing event on your Google Calendar.",
    use_when="When you need to change the details of an existing event, like its time, title, or location.",
    side_effects="The specified event on your primary Google Calendar will be modified."
)

@mcp.tool(description=UpdateEventToolDescription.model_dump_json())
async def update_calendar_event(
    event_id: Annotated[str, Field(description="The ID of the event to update.")],
    summary: Annotated[Optional[str], Field(description="The new title or summary of the event.")] = None,
    start_time: Annotated[Optional[str], Field(description="The new start time in ISO 8601 format.")] = None,
    end_time: Annotated[Optional[str], Field(description="The new end time in ISO 8601 format.")] = None,
    location: Annotated[Optional[str], Field(description="The new location of the event.")] = None,
    description: Annotated[Optional[str], Field(description="The new description of the event.")] = None
) -> str:
    """Updates an existing event on the user's primary calendar."""
    service = get_calendar_service()
    try:
        event = service.events().get(calendarId='primary', eventId=event_id).execute()

        if summary:
            event['summary'] = summary
        if location:
            event['location'] = location
        if description:
            event['description'] = description
        if start_time:
            event['start']['dateTime'] = start_time
        if end_time:
            event['end']['dateTime'] = end_time

        updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
        return f"Event updated successfully. View it here: {updated_event.get('htmlLink')}"
    except HttpError as error:
        return f"An error occurred: {error}"

# Tool: Delete Event
DeleteEventToolDescription = RichToolDescription(
    description="Deletes an event from your Google Calendar.",
    use_when="When you want to cancel or remove an event from your schedule.",
    side_effects="The specified event will be permanently removed from your primary Google Calendar."
)

@mcp.tool(description=DeleteEventToolDescription.model_dump_json())
async def delete_calendar_event(
    event_id: Annotated[str, Field(description="The ID of the event to delete.")]
) -> str:
    """Deletes an event from the user's primary calendar."""
    service = get_calendar_service()
    try:
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return "Event deleted successfully."
    except HttpError as error:
        return f"An error occurred: {error}"


@mcp.tool
async def validate() -> str:
    """
    NOTE: This tool must be present in an MCP server used by puch for validation.
    """
    return MY_NUMBER

async def main():
    print("Starting MCP server on http://0.0.0.0:8085")
    print("Make sure to use a tool like ngrok to make it publicly accessible.")
    await mcp.run_async(
        "streamable-http",
        host="0.0.0.0",
        port=8085,
    )


if __name__ == "__main__":
    asyncio.run(main())