# main.py
import sqlite3
from datetime import date

from database import get_connection, ensure_schema, insert_meal_record, get_today_record, get_all_records
from validation import validate_date, validate_meals
from views import print_menu, print_table, print_message


def read_int(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print_message(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print_message(f"Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print_message("Invalid input. Please enter an integer.")


def add_entry():
    print_message("\n--- Add New Meal Entry ---")

    # Date input
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            date_str = validate_date(date_str)
            break
        except ValueError as e:
            print_message(str(e))

    # Meals input
    while True:
        prepared = read_int("Meals prepared: ", min_value=1)
        served = read_int("Meals served: ", min_value=1, max_value=prepared)
        consumed = read_int("Meals consumed: ", min_value=1, max_value=served)

        try:
            validated = validate_meals(prepared, served, consumed)
            break
        except ValueError as e:
            print_message(str(e))

    food_waste = validated["food_waste"]

    # Insert into DB
    conn = get_connection()
    try:
        insert_meal_record(
            conn,
            date_str,
            validated["meals_prepared"],
            validated["meals_served"],
            validated["meals_consumed"],
            food_waste,
        )
        print_message("\nEntry saved successfully.")
        print_message(f"Food waste for {date_str}: {food_waste} meals.")
    except sqlite3.IntegrityError:
        print_message("\nError: An entry for this date already exists or DB constraint failed.")
    finally:
        conn.close()


def show_today():
    print_message("\n--- Today's Entry ---")
    today = date.today().isoformat()
    conn = get_connection()
    record = get_today_record(conn, today)
    conn.close()

    if not record:
        print_message("No entry found for today.")
        return

    headers = ["Date", "Prepared", "Served", "Consumed", "Waste"]
    rows = [
        [
            record["date"],
            record["meals_prepared"],
            record["meals_served"],
            record["meals_consumed"],
            record["food_waste"],
        ]
    ]
    print_table(headers, rows)


def show_all():
    print_message("\n--- All Meal Entries ---")
    conn = get_connection()
    records = get_all_records(conn)
    conn.close()

    if not records:
        print_message("No entries found in the database.")
        return

    headers = ["Date", "Prepared", "Served", "Consumed", "Waste"]
    rows = [
        [
            r["date"],
            r["meals_prepared"],
            r["meals_served"],
            r["meals_consumed"],
            r["food_waste"],
        ]
        for r in records
    ]
    print_table(headers, rows)


def main():
    # Ensure DB and schema
    conn = get_connection()
    ensure_schema(conn)
    conn.close()

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_today()
        elif choice == "3":
            show_all()
        elif choice == "4":
            print_message("\nExiting program.")
            break
        else:
            print_message("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()