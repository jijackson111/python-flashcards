import sqlite3
from database import get_connection

# Get list of decks
def get_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return tables
    
# Add deck

# Remove deck