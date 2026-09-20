# config.py

DATABASE_PATH = "data/mess_meal_tracker.db"
DB_FOLDER = "data"

DATE_FORMAT = "%Y-%m-%d"

MESSAGES = {
    "title": "=" * 50 + "\n          MESS MEAL TRACKER\n" + "=" * 50,
    "invalid_date": "\nError: Invalid date format. Use YYYY-MM-DD.",
    "invalid_number": "\nError: Please enter whole numbers only.",
    "saved_success": "\nMeal record saved successfully.",
    "no_records_today": "\nNo records found for today.",
    "no_records_all": "\nNo records found in database.",
}