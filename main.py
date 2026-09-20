# main.py

from config import MESSAGES
from views import display_title, display_menu, display_record, display_all_records, display_success, display_error
from validation import validate_date, validate_positive_integer, validate_logical_constraints
from calculations import calculate_waste
from database import initialize_database, add_record, get_today_record, get_all_records
from stats import display_statistics

def get_meal_input():
    """Get meal record input from user."""
    print("\n--- Add Meal Record ---")
    
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        display_error(MESSAGES["invalid_date"])
        return None
    
    try:
        prepared = int(input("Enter meals prepared: ").strip())
        served = int(input("Enter meals served: ").strip())
        consumed = int(input("Enter meals consumed: ").strip())
    except ValueError:
        display_error(MESSAGES["invalid_number"])
        return None
    
    if not validate_positive_integer(str(prepared)) or \
       not validate_positive_integer(str(served)) or \
       not validate_positive_integer(str(consumed)):
        display_error("Values cannot be negative.")
        return None
    
    if not validate_logical_constraints(prepared, served, consumed):
        display_error("Invalid values: served cannot exceed prepared, consumed cannot exceed served.")
        return None
    
    waste = calculate_waste(prepared, consumed)
    
    return {
        "date": date,
        "prepared": prepared,
        "served": served,
        "consumed": consumed,
        "waste": waste
    }

def main():
    """Main application loop."""
    initialize_database()
    
    while True:
        display_title()
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            data = get_meal_input()
            if data:
                add_record(data["date"], data["prepared"], data["served"], data["consumed"], data["waste"])
                display_success()
        
        elif choice == "2":
            record = get_today_record()
            display_record(record)
        
        elif choice == "3":
            records = get_all_records()
            display_all_records(records)
        
        elif choice == "4":
            print("\nExiting. Thank you for using Mess Meal Tracker!")
            break
        
        else:
            display_error("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()