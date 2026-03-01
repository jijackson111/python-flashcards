import sqlite3
from database import init_db, get_connection
from decks import get_decks
from cards import add_card

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
    return table_choice
