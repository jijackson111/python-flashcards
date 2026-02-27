import sqlite3
from database import get_connection

# Add card
def add_card(card_data, deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = f"INSERT INTO {deck} (front, back, difficulty) VALUES (?, ?, ?)"
        cursor.execute(query, card_data)
        conn.commit()

# Remove card

# Use card