import sqlite3
from database import init_db, get_connection
from decks import get_decks
import cards
import random

# Initalise database
init_db()

# Display list of tables to user and have them pick which they would like to use
def pick_table():
    table_list = [table[0] for table in get_decks()]
    print("List of available decks:")
    for i in range(len(table_list)):
        table_name = table_list[i]
        print(f"   {i+1}. {table_name}")
    table_choice = int(input("Enter the deck you would like to use: "))
    return table_list[table_choice-1]

deck = "cards"

# Start study session
def run_study_session(card_list, deck):
    card = random.choice(card_list)
    print(f"\nFRONT: {card.get_card()}")
    input("Press any key to flip...")
    card.flip()
    print(f"BACK: {card.get_card()}")
    cmd = input("Did you get it right (y/n)")
    if cmd == 'y':
        card.update_difficulty(deck)
        print(card)

card_list = cards.get_all_cards(deck)
run_study_session(card_list, deck)