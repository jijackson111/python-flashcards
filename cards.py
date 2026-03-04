import sqlite3
from database import get_connection

# Flashcard object
class Flashcard:
    def __init__(self, front, back, deck, difficulty=1, card_id=None):
        self.card_id = card_id
        self.front = front
        self.back = back
        self.difficulty = difficulty
        self.is_flipped = False
        self.deck = deck
    
    # Print card
    def get_card(self):
        if self.is_flipped == False:
            return self.front
        else:
            return self.back
    
    # Flip card
    def flip(self):
        self.is_flipped = not self.is_flipped

    # Update difficulty
    def update_difficulty(self, deck, known=True):
        # Put difficulty to 0 if user knew answer
        if known:
            self.difficulty = 0
            with get_connection() as conn:
                cursor = conn.cursor()
                query = f"UPDATE {deck} SET difficulty = ? WHERE id = ?"
                cursor.execute(query, (self.difficulty, self.card_id))
                conn.commit()
    
    # Print card
    def __str__(self):
        return f"Card: {self.front} ({self.back})| Difficulty: {self.difficulty}"
    
    # Return card as tuple
    def get_object(self):
        return (self.front, self.back, self.difficulty)

# Add card
def add_card(card_obj, deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = f"INSERT INTO {deck} (front, back, difficulty) VALUES (?, ?, ?)"
        cursor.execute(query, card_obj)
        conn.commit()

# Remove card
def remove_card(card_front, deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = f"DELETE FROM {deck} WHERE front=?"
        cursor.execute(query, (card_front,))
        conn.commit()

# Get all cards and return as Flashcard object
def get_all_cards(deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM {deck}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Flashcard(row[1], row[2], deck, row[3], row[0]) for row in rows]
