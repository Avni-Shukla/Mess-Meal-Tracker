import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data") / "mess_meal_tracker.db"


def get_connection():
    Path("data").mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meal_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            meal_date TEXT NOT NULL,
            meal_type TEXT NOT NULL,
            menu_name TEXT NOT NULL,
            prepared_count INTEGER NOT NULL,
            served_count INTEGER NOT NULL,
            unserved_waste INTEGER NOT NULL,
            estimated_plate_waste INTEGER NOT NULL,
            total_waste INTEGER NOT NULL,
            waste_percentage REAL NOT NULL,
            waste_reason TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()