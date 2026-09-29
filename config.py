# config.py - Configuration settings for Mess Meal Tracker

# Database settings
DATABASE_PATH = "data/mess_meal_tracker.db"
DB_NAME = "data/mess_meal_tracker.db"
DB_TABLE = "meal_records"

# Messages dictionary
MESSAGES = {
    "welcome": "MESS MEAL TRACKER",
    "title": "MESS MEAL TRACKER",
    "menu": """
1. Add Meal Record
2. View Today's Record
3. View All Records
4. Exit
""",
    "success": "✓ Record saved successfully!",
    "saved_success": "✓ Record saved successfully!",
    "error": "✗ Error occurred!",
    "not_found": "No record found!",
    "no_records_today": "No records found for today.",
    "no_records": "No records found in database.",
    "goodbye": "Thank you for using Mess Meal Tracker. Goodbye!"
}

# Date format
DATE_FORMAT = "%Y-%m-%d"