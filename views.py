# views.py - Display functions for Mess Meal Tracker

from config import MESSAGES

def display_title():
    """Print top title banner."""
    print("\n==============================")
    print(f"      {MESSAGES['title']}      ")
    print("==============================")

def display_menu():
    """Print application menu."""
    display_title()
    print(MESSAGES["menu"].strip())
    print("==============================")

def display_success(message: str):
    """Display success message."""
    print(f"✓ {message}")

def display_error(message: str):
    """Display error message."""
    print(f"❌ {message}")

def display_record(record):
    """Display a single day's record."""
    if not record:
        print(f"\nℹ {MESSAGES['no_records_today']}")
        return
    print("\nDate        | Prepared | Served | Consumed | Waste")
    print("-" * 52)
    print(f"{record[0]:<11} | {record[1]:<8} | {record[2]:<6} | {record[3]:<8} | {record[4]}")

def display_all_records(records, stats):
    """Display all historical records in tabular format with summary stats."""
    if not records:
        print(f"\nℹ {MESSAGES['no_records']}")
        return
    
    print("\nDate        | Prepared | Served | Consumed | Waste")
    print("-" * 52)
    for r in records:
        print(f"{r[0]:<11} | {r[1]:<8} | {r[2]:<6} | {r[3]:<8} | {r[4]}")
    print("-" * 52)
    print(f"Total: {stats['total_records']} records | Total Waste: {stats['total_waste']} meals | Avg Waste: {stats['avg_waste']} meals/day")