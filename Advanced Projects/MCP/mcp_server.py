from mcp.server.fastmcp import FastMCP
import mysql.connector
import sys # Import sys for stderr
from datetime import date, datetime

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "mcp_user",
    "password": "Coke@0929", # Make sure this matches your actual user password
    "database": "MCP_TEST"
}

def get_connection():
    """Establishes and returns a new MySQL database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        # Print error to stderr so Claude Desktop can log it
        print(f"Database connection error: {err}", file=sys.stderr)
        raise # Re-raise the exception to inform the calling tool

mcp = FastMCP("MySQL MCP Server")

# --- TABLE CREATIOON TOOL ---

@mcp.tool()
def create_game_tables() -> dict:
    """
    Creates the 'games_owned' and 'current_games_played' tables in the database.
    This should be run once after setting up the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Table for all owned games
        create_games_owned_table_sql = """
        CREATE TABLE IF NOT EXISTS games_owned (
            game_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            rating DECIMAL(3,1),
            max_players INT,
            game_type VARCHAR(100)
        );
        """
        cursor.execute(create_games_owned_table_sql)

        # Table for games currently being played (with foreign key to games_owned)
        create_current_games_played_table_sql = """
        CREATE TABLE IF NOT EXISTS current_games_played (
            id INT AUTO_INCREMENT PRIMARY KEY,
            game_id INT NOT NULL,
            play_status VARCHAR(50) DEFAULT 'Playing',
            started_playing_date DATE,
            last_played DATETIME,
            FOREIGN KEY (game_id) REFERENCES games_owned(game_id) ON DELETE CASCADE
        );
        """
        cursor.execute(create_current_games_played_table_sql)
        conn.commit()
        return {"status": "success", "message": "Tables 'games_owned' and 'current_games_played' created or already exist."}
    except mysql.connector.Error as err:
        print(f"Error creating game tables: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

# --- CRUD Operations for Games Owned ---

@mcp.tool()
def create_game_owned(name: str, rating: float, max_players: int, game_type: str) -> dict:
    """Adds a new game to the 'games_owned' list."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO games_owned (name, rating, max_players, game_type) VALUES (%s, %s, %s, %s)",
            (name, rating, max_players, game_type)
        )
        conn.commit()
        game_id = cursor.lastrowid
        return {"status": "success", "game_id": game_id, "name": name}
    except mysql.connector.Error as err:
        print(f"Error creating game owned: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def read_game_owned(game_id: int = None, name: str = None) -> dict:
    """
    Reads a game from 'games_owned' by ID or name.
    Provide either game_id or name.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        if game_id:
            cursor.execute("SELECT * FROM games_owned WHERE game_id = %s", (game_id,))
        elif name:
            cursor.execute("SELECT * FROM games_owned WHERE name = %s", (name,))
        else:
            return {"status": "error", "message": "Please provide either 'game_id' or 'name'."}

        result = cursor.fetchone()
        if result:
            return result
        return {"status": "not found"}
    except mysql.connector.Error as err:
        print(f"Error reading game owned: {err}", file=sys.stderr)
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def update_game_owned(game_id: int, new_name: str = None, new_rating: float = None, new_max_players: int = None, new_game_type: str = None) -> dict:
    """Updates properties of a game in 'games_owned' by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        if new_name is not None:
            updates.append("name = %s")
            params.append(new_name)
        if new_rating is not None:
            updates.append("rating = %s")
            params.append(new_rating)
        if new_max_players is not None:
            updates.append("max_players = %s")
            params.append(new_max_players)
        if new_game_type is not None:
            updates.append("game_type = %s")
            params.append(new_game_type)

        if not updates:
            return {"status": "info", "message": "No fields provided for update."}

        sql = f"UPDATE games_owned SET {', '.join(updates)} WHERE game_id = %s"
        params.append(game_id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        affected = cursor.rowcount
        return {"status": "success" if affected else "not found", "affected_rows": affected}
    except mysql.connector.Error as err:
        print(f"Error updating game owned: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def delete_game_owned(game_id: int) -> dict:
    """Deletes a game from the 'games_owned' list by ID.
    Note: Due to ON DELETE CASCADE, any entries in current_games_played
    referencing this game_id will also be deleted.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM games_owned WHERE game_id = %s", (game_id,))
        conn.commit()
        affected = cursor.rowcount
        return {"status": "success" if affected else "not found", "affected_rows": affected}
    except mysql.connector.Error as err:
        print(f"Error deleting game owned: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

# --- CRUD Operations for Current Games Played ---

@mcp.tool()
def add_current_game_played(game_id: int, play_status: str = 'Playing', started_playing_date: str = None) -> dict:
    """
    Adds a game to the 'current_games_played' list.
    game_id must refer to an existing game in 'games_owned'.
    started_playing_date should be in 'YYYY-MM-DD' format.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Validate game_id exists in games_owned
        cursor.execute("SELECT game_id FROM games_owned WHERE game_id = %s", (game_id,))
        if not cursor.fetchone():
            return {"status": "error", "message": f"Game with ID {game_id} not found in games_owned."}

        start_date_obj = date.today()
        if started_playing_date:
            try:
                start_date_obj = date.fromisoformat(started_playing_date)
            except ValueError:
                return {"status": "error", "message": "Invalid date format for started_playing_date. Use YYYY-MM-DD."}

        cursor.execute(
            "INSERT INTO current_games_played (game_id, play_status, started_playing_date, last_played) VALUES (%s, %s, %s, %s)",
            (game_id, play_status, start_date_obj, datetime.now())
        )
        conn.commit()
        current_game_id = cursor.lastrowid
        return {"status": "success", "current_game_id": current_game_id, "game_id": game_id}
    except mysql.connector.Error as err:
        print(f"Error adding current game played: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def get_current_games_played() -> list:
    """Reads all entries from 'current_games_played', joining with 'games_owned' for game details."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
        SELECT c.id, g.name AS game_name, g.rating, g.max_players, g.game_type,
               c.play_status, c.started_playing_date, c.last_played
        FROM current_games_played c
        JOIN games_owned g ON c.game_id = g.game_id;
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Error getting current games played: {err}", file=sys.stderr)
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def update_current_game_played(id: int, new_play_status: str = None, new_last_played_date: str = None) -> dict:
    """
    Updates the status or last played date of a game in 'current_games_played'.
    new_last_played_date should be in 'YYYY-MM-DD' format.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        if new_play_status is not None:
            updates.append("play_status = %s")
            params.append(new_play_status)
        if new_last_played_date is not None:
            try:
                last_played_obj = datetime.fromisoformat(new_last_played_date).replace(hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second, microsecond=datetime.now().microsecond)
                updates.append("last_played = %s")
                params.append(last_played_obj)
            except ValueError:
                return {"status": "error", "message": "Invalid date format for new_last_played_date. Use YYYY-MM-DD."}
        else: # Update last_played to now if no specific date is given
            updates.append("last_played = %s")
            params.append(datetime.now())


        if not updates:
            return {"status": "info", "message": "No fields provided for update."}

        sql = f"UPDATE current_games_played SET {', '.join(updates)} WHERE id = %s"
        params.append(id)

        cursor.execute(sql, tuple(params))
        conn.commit()
        affected = cursor.rowcount
        return {"status": "success" if affected else "not found", "affected_rows": affected}
    except mysql.connector.Error as err:
        print(f"Error updating current game played: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

@mcp.tool()
def remove_current_game_played(id: int) -> dict:
    """Removes a game from 'current_games_played' list by its current_game_id."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM current_games_played WHERE id = %s", (id,))
        conn.commit()
        affected = cursor.rowcount
        return {"status": "success" if affected else "not found", "affected_rows": affected}
    except mysql.connector.Error as err:
        print(f"Error removing current game played: {err}", file=sys.stderr)
        conn.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    mcp.run(transport="stdio")

