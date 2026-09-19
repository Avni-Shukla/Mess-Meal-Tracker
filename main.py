from calculations import (
    calculate_unserved_waste,
    calculate_total_waste,
    calculate_waste_percentage
)

from validation import validate_meal_values
from database import create_table

def main():
    create_table()

    print("=" * 50)
    print("          MESS MEAL TRACKER")
    print("=" * 50)

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


if __name__ == "__main__":
    main()