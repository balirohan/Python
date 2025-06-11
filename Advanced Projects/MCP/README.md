# MySQL MCP Server for Game Database Management with Claude Desktop

This repository contains the backend server and configuration for an MCP (Model Context Protocol) server that integrates with a MySQL database to manage video game collections. It allows you to track games you own and games you are currently playing, using Claude Desktop as a client.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Prerequisites](#prerequisites)
4.  [Setup Guide](#setup-guide)
    * [1. MySQL Database Setup](#1-mysql-database-setup)
    * [2. Python Server Setup](#2-python-server-setup)
    * [3. Claude Desktop Configuration](#3-claude-desktop-configuration)
5.  [Usage](#usage)
    * [Person Management Tools](#person-management-tools)
    * [Game Management Tools](#game-management-tools)
6.  [Troubleshooting](#troubleshooting)
7.  [Contributing](#contributing)
8.  [License](#license)

## Introduction

This project demonstrates a client-server architecture where a Python-based MCP server interacts with a MySQL database. The server exposes various "tools" (functions) that can be called by an MCP client, such as Claude Desktop.

The primary focus of the server is to manage your `video game collection`, categorizing games into those you `own` and those you are `currently playing`.

## Features

* **Game Collection Management:**
    * `games_owned` table: Stores details of all video games you own (name, rating, max players, type).
    * `current_games_played` table: Tracks games you are actively playing, linked to `games_owned` via a foreign key.
    * CRUD operations for both game tables.
* **Database Interaction:** Uses `mysql.connector` to connect to and manage a MySQL database.
* **MCP Server:** Implemented using `fastmcp` for communication with an MCP client like Claude Desktop.

## Prerequisites

Before setting up the project, ensure you have the following installed:

* **MySQL Server:** A running MySQL database instance.
    * [Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
* **Python 3:** Version 3.8 or higher is recommended.
    * [Python Downloads](https://www.python.org/downloads/)
    * On macOS, `brew install python` (via Homebrew) is a common way to install.
* **Claude Desktop:** The client application that will interact with your MCP server.
    * Ensure you have the Claude Desktop application installed.

## Setup Guide

Follow these steps carefully to get your MCP server and Claude Desktop client communicating.

### 1. MySQL Database Setup

Ensure your MySQL server is running and configure the database and user.

1.  **Start MySQL Server:**
    On macOS, go to **System Settings > MySQL** and ensure the server status is "Running."

2.  **Connect to MySQL as Root:**
    Open your Terminal and connect to your MySQL server with root privileges:

    ```bash
    mysql -u root -p
    ```
    Enter your MySQL root password when prompted.

3.  **Create Database and User:**
    Execute the following SQL commands to create the `MCP_TEST` database and the `mcp_user` with the specified password and all necessary privileges.

    ```sql
    -- Create the database if it doesn't exist
    CREATE DATABASE IF NOT EXISTS MCP_TEST;

    -- Create the user if it doesn't exist.
    -- IMPORTANT: 'localhost' means the user can only connect from the same machine.
    -- If your MySQL is on a different host, adjust 'localhost' accordingly.
    CREATE USER IF NOT EXISTS 'mcp_user'@'localhost' IDENTIFIED BY 'Coke@0929';

    -- Grant all privileges to 'mcp_user' on the 'MCP_TEST' database
    GRANT ALL PRIVILEGES ON MCP_TEST.* TO 'mcp_user'@'localhost';

    -- Apply the changes
    FLUSH PRIVILEGES;
    ```
    You can exit the MySQL client by typing `exit;`.

### 2. Python Server Setup

This involves setting up your Python environment and installing the required libraries.

1.  **Save the Server Script:**
    Save the provided Python code as `mcp_server.py` in your desired project directory, for example:
    `/Users/balir/My Documents/My Repositories/Python/Advanced Projects/MCP/mcp_server.py`

2.  **Identify the Python Interpreter for Claude Desktop:**
    Claude Desktop needs the *absolute path* to the Python interpreter it should use. Open your Terminal and find the path to your `python3` (or the specific Python installation you want Claude Desktop to use):

    ```bash
    which python3
    ```
    Example output: `/opt/homebrew/bin/python3` or `/usr/local/bin/python3` or `/usr/bin/python3`. **Copy this full path.**

3.  **Install Python Dependencies into that Specific Interpreter:**
    Use the *full path* from the previous step to install `fastmcp` and `mysql-connector-python`:

    ```bash
    /opt/homebrew/bin/python3 -m pip install fastmcp mysql-connector-python
    ```
    (Replace `/opt/homebrew/bin/python3` with the actual path you found).

4.  **Test the Python Server (Optional but Recommended):**
    Open a new Terminal window and run your `mcp_server.py` directly using the same full Python path:

    ```bash
    /opt/homebrew/bin/python3 '/Users/balir/My Documents/My Repositories/Python/Advanced Projects/MCP/mcp_server.py'
    ```
    (Replace paths as necessary).
    The script should run without any error output and simply appear to "hang" or sit idle. This is expected behavior for an `stdio` MCP server, indicating it's ready to receive commands. **Leave this Terminal window open.**

### 3. Claude Desktop Configuration

Now, configure Claude Desktop to recognize and connect to your MCP server.

1.  **Locate `claude_desktop_config.json`:**
    This file is typically located within Claude Desktop's application data folder. A common path on macOS is `~/Library/Application Support/Claude Desktop/`. You may need to enable hidden files in Finder (`Command + Shift + .`) or use Terminal to navigate.

2.  **Edit `claude_desktop_config.json`:**
    Open this file using a text editor (like `nano` in Terminal, VS Code, etc.).
    **Ensure the JSON syntax is perfectly valid.** Add or modify the `"mcpServers"` block as follows.

    ```json
      {
      "mcpServers": {
        "mysql_crud": {
          "command": "/opt/homebrew/bin/python3", // <-- REPLACE WITH YOUR ACTUAL PYTHON PATH (from Step 2.2)
          "args": [
            "/Users/balir/My Documents/My Repositories/Python/Advanced Projects/MCP/mcp_server.py" // <-- ENSURE THIS PATH IS CORRECT
          ]
        }
      }
    }
    ```
    **Important:** The `"command"` value must be the **full, absolute path** to the Python interpreter that has `fastmcp` installed. The `"args"` value must be the **full, absolute path** to your `mcp_server.py` script.

3.  **Save the `claude_desktop_config.json` file.**

4.  **Completely Quit Claude Desktop:**
    This is crucial for Claude Desktop to reload its configuration. On macOS, press `Command + Q` or right-click the Dock icon and select "Quit".

5.  **Relaunch Claude Desktop.**

## Usage

Once Claude Desktop relaunches, it should detect your `mysql_crud` server. You can now use the exposed tools.


### Game Management Tools

1.  **Create Game Tables (Run this once!):**
    Before adding any game data, you need to create the `games_owned` and `current_games_played` tables.
    * **Tool Call:** `create_game_tables()`
    * **Expected Response:** `{"status": "success", "message": "Tables 'games_owned' and 'current_games_played' created or already exist."}`

2.  **Add Owned Games:**
    * `create_game_owned(name="The Witcher 3", rating=9.5, max_players=1, game_type="RPG")`
    * `create_game_owned(name="Overwatch 2", rating=7.0, max_players=5, game_type="FPS")`
    * `create_game_owned(name="Minecraft", rating=10.0, max_players=8, game_type="Sandbox")`

3.  **Read Owned Games:**
    * `read_game_owned(name="The Witcher 3")`
    * `read_game_owned(game_id=1)` (assuming 'The Witcher 3' got ID 1)

4.  **Update Owned Games:**
    * `update_game_owned(game_id=2, new_rating=7.5, new_game_type="Hero Shooter")`

5.  **Delete Owned Games:**
    * `delete_game_owned(game_id=3)`

6.  **Add Current Games Played:**
    * `add_current_game_played(game_id=1, play_status="Playing", started_playing_date="2024-05-15")`
    * `add_current_game_played(game_id=2, play_status="Paused")`

7.  **Get All Current Games Played:**
    * `get_current_games_played()`

8.  **Update Current Game Status/Last Played:**
    * `update_current_game_played(id=1, new_play_status="Finished")`
    * `update_current_game_played(id=2, new_last_played_date="2024-06-10")`

9.  **Remove Current Game from List:**
    * `remove_current_game_played(id=1)`
  
## Screenshots
<img src="https://github.com/user-attachments/assets/99dd5914-859f-4ac6-a97d-32c6f90cc0b1" alt="Screenshot of macOS Terminal" width="500">
<img src="https://github.com/user-attachments/assets/fdab8195-b473-436c-a5ad-1b547feac58c" alt="Screenshot of Claude Desktop" width="500">
<img src="https://github.com/user-attachments/assets/3a5a0766-6a2e-4a73-8a58-a2f7163bf578" alt="Screenshot of Claude Desktop" width="500">
<img src="https://github.com/user-attachments/assets/01a9b9d4-bfbf-47c7-a322-3f16763a1610" alt="Screenshot of macOS Terminal" width="500">
<img src="https://github.com/user-attachments/assets/cd349fbf-aba2-4df6-8bff-a05fe94d08e4" alt="Screenshot of Claude Desktop" width="500">
<img src="https://github.com/user-attachments/assets/8f26a953-251f-4031-b120-420a9767b93d" alt="Screenshot of Claude Desktop" width="500">


## Special Mention
I told Claude to create an entry into my current_games_played table, but it was smart enough to know that it had to first create the same entry into my games_owned table before executing my order.
The future looks bright!


## Troubleshooting

* **`spawn python ENOENT` error in Claude Desktop logs:** Claude Desktop cannot find the Python executable. Ensure the `command` path in `claude_desktop_config.json` is the full, absolute path to your `python3` interpreter.
* **`ModuleNotFoundError: No module named 'mcp'` in Claude Desktop logs:** The Python interpreter Claude Desktop is using does not have `fastmcp` (or other required modules) installed. Run the `pip install` command using the *exact full path* to that Python interpreter (see Section 2.3).
* **`[Errno 2] No such file or directory` for `mcp_server.py`:** The path to `mcp_server.py` in `claude_desktop_config.json` is incorrect. Double-check the filename (`mcp_server.py`) and the full directory path.
* **Database connection errors (e.g., `Access denied`, `Unknown database`, `Can't connect to MySQL server`):**
    * Ensure MySQL server is running.
    * Verify `DB_CONFIG` (host, user, password, database) in `mcp_server.py` matches your MySQL setup.
    * Confirm `mcp_user` has all privileges granted on `MCP_TEST.*`.
* **`SyntaxError: invalid syntax` in `mcp_server.py`:** You likely have non-Python code (like a file path) accidentally copied into your script. Check the line number mentioned in the traceback in your `mcp_server.py` file and remove or correct it.
* **Server disconnects early (general):** Look at the stderr output in your Claude Desktop logs. The Python script prints errors to `sys.stderr`, which Claude Desktop captures, providing more specific Python tracebacks.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE.md).

