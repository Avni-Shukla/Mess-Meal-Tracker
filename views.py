# views.py

from config import MESSAGES

def display_title():
    """Display the application title."""
    print(MESSAGES["title"])

def display_menu():
    """Display the main menu."""
    print("\n1. Add Meal Record")
    print("2. View Today's Record")
    print("3. View All Records")
    print("4. Exit")

def display_record(record):
    """Display a single meal record."""
    if not record:
        print(MESSAGES["no_records_today"])
        return
    
    print(f"\nDate: {record[1]}")
    print(f"Meals Prepared: {record[2]}")
    print(f"Meals Served: {record[3]}")
    print(f"Meals Consumed: {record[4]}")
    print(f"Food Waste: {record[5]}")

def display_all_records(records):
    """Display all meal records."""
    if not records:
        print(MESSAGES["no_records_all"])
        return
    
    print("\n" + "=" * 50)
    print("ALL MEAL RECORDS")
    print("=" * 50)
    
    for record in records:
        print(f"\nID: {record[0]}")
        print(f"Date: {record[1]}")
        print(f"Prepared: {record[2]} | Served: {record[3]} | Consumed: {record[4]} | Waste: {record[5]}")
    
    print("\n" + "=" * 50)

def display_success():
    """Display success message."""
    print(MESSAGES["saved_success"])

def display_error(message):
    """Display an error message."""
    print(f"\nError: {message}")