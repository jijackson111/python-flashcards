import sqlite3
from database import get_connection

# Get list of decks
def get_decks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return tables
    
# Add deck
def add_deck(deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        # Check if table already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (deck,))
        if cursor.fetchone():
            return f"Error: Deck '{deck}' already exists."
        # Add table
        try:
            cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {deck} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
            return f"Deck {deck} was created successfully" 
        except Exception as e:
            return f"Error occured: {e}"

# Remove deck
def remove_deck(deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (deck,))
        if not cursor.fetchone():
            return f"Error: Deck '{deck}' does not exist."
        # Remove table
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {deck}")
            return f"Deck {deck} was deleted successfully"
        except Exception as e:
            return f"Error occured: {e}"