import sqlite3
from database import get_connection

# Flashcard object
class Flashcard:
    def __init__(self, front, back, difficulty=1, card_id=None):
        self.card_id = card_id
        self.front = front
        self.back = back
        self.difficulty = difficulty
        self.is_flipped = False
    
    # Get card
    def get_card(self):
        if self.is_flipped == False:
            return self.front
        else:
            return self.back
    
    # Flip card
    def flip(self):
        self.is_flipped = not self.is_flipped

    # Update difficulty
    def update_difficulty(self, known=True):
        # Put difficulty to 0 if user knew answer
        if known:
            self.difficulty = 0
    
    # Print card
    def __str__(self):
        return f"Card: {self.front} ({self.back})| Difficulty: {self.difficulty}"

# Add card
def add_card(card_obj, deck):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = f"INSERT INTO {deck} (front, back, difficulty) VALUES (?, ?, ?)"
        cursor.execute(query, card_obj)
        conn.commit()

# Remove card

# Use card

my_card = Flashcard("example3", "theback")
print(my_card.get_card())
my_card.flip()
print(my_card.get_card())