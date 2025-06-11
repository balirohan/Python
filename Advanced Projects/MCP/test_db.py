import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "mcp_user",
    "password": "Coke@0929",
    "database": "MCP_TEST"
}

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    if conn.is_connected():
        print("Successfully connected to MySQL database!")
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        print(f"Connected to database: {db_name}")
    else:
        print("Failed to connect to MySQL database.")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection closed.")