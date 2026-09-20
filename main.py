from database import save_meal_record
from calculations import (
    calculate_unserved_waste,
    calculate_total_waste,
    calculate_waste_percentage
)

from validation import validate_meal_values
from database import create_table
from datetime import date

def main():
    create_table()

    print("=" * 50)
    print("          MESS MEAL TRACKER")
    print("=" * 50)

# Get today's date
    today = date.today().isoformat()  # e.g. "2026-09-20"
    print(f"\nDate: {today}")
    confirm = input("Use this date? (y/n): ").strip().lower()
    if confirm != "y":
        custom_date = input("Enter date (YYYY-MM-DD): ").strip()
        if len(custom_date) != 10 or custom_date[4] != "-" or custom_date[7] != "-":
            print("\nError: Invalid date format. Use YYYY-MM-DD.")
            return
        today = custom_date

    try:
        prepared = int(input("Enter portions prepared: "))
        served = int(input("Enter portions served: "))
        plate_waste = int(input("Enter estimated plate waste: "))

    except ValueError:
        print("\nError: Please enter whole numbers only.")
        return

    is_valid, message = validate_meal_values(
        prepared,
        served,
        plate_waste
    )

    if not is_valid:
        print(f"\nError: {message}")
        return

    unserved_waste = calculate_unserved_waste(prepared, served)
    total_waste = calculate_total_waste(unserved_waste, plate_waste)
    waste_percentage = calculate_waste_percentage(total_waste, prepared)

    print("\n--- FOOD WASTE SUMMARY ---")
    print(f"Unserved waste: {unserved_waste} portions")
    print(f"Estimated plate waste: {plate_waste} portions")
    print(f"Total waste: {total_waste} portions")
    print(f"Waste percentage: {waste_percentage}%")
    save_meal_record(
        today,
        prepared,
        served,
        plate_waste,
        unserved_waste,
        total_waste,
        waste_percentage
    )


    print("\nMeal record saved successfully.")



if __name__ == "__main__":
    main()
