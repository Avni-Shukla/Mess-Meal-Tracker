DB_NAME = "data/mess_meal_tracker.db"
import sqlite3
from pathlib import Path
from datetime import date


DATABASE_PATH = Path("data") / "mess_meal_tracker.db"


def get_connection():
    Path("data").mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        prepared INTEGER NOT NULL,
        served INTEGER NOT NULL,
        plate_waste INTEGER NOT NULL,
        unserved_waste INTEGER NOT NULL,
        total_waste INTEGER NOT NULL,
        waste_percentage REAL NOT NULL
    )
""")
        
    connection.commit()
    connection.close()


def save_meal_record(date_str, prepared, served, plate_waste, unserved_waste, total_waste, waste_percentage):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO meal_records (
            date,
            prepared,
            served,
            plate_waste,
            unserved_waste,
            total_waste,
            waste_percentage
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        date_str,
        prepared,
        served,
        plate_waste,
        unserved_waste,
        total_waste,
        waste_percentage
    ))

    connection.commit()
    connection.close()

def view_today_records():
    from datetime import date
    connection = get_connection()
    cursor = connection.cursor()

    today = date.today().isoformat()

    cursor.execute("""
        SELECT id, prepared, served, plate_waste, unserved_waste, total_waste, waste_percentage
        FROM meal_records
        WHERE date = ?
        ORDER BY id
    """, (today,))

    rows = cursor.fetchall()
    connection.close()

    if not rows:
        print(f"\nNo records found for today ({today}).")
        return

    print(f"\n--- Today's Records ({today}) ---")
    for row in rows:
        id_, prepared, served, plate_waste, unserved_waste, total_waste, waste_pct = row
        print(f"ID {id_}: Prepared={prepared}, Served={served}, Plate waste={plate_waste}, "
              f"Unserved={unserved_waste}, Total waste={total_waste}, Waste%={waste_pct:.2f}%")  

def view_all_records():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, date, prepared, served, plate_waste, unserved_waste, total_waste, waste_percentage
        FROM meal_records
        ORDER BY date, id
    """)

    rows = cursor.fetchall()
    connection.close()

    if not rows:
        print("\nNo records found in database.")
        return

    print("\n--- All Records ---")
    for row in rows:
        id_, date_, prepared, served, plate_waste, unserved_waste, total_waste, waste_pct = row
        date_display = date_ if date_ else "NO DATE"
        print(f"[{date_display}] ID {id_}: Prepared={prepared}, Served={served}, "
              f"Plate waste={plate_waste}, Unserved={unserved_waste}, "
              f"Total waste={total_waste}, Waste%={waste_pct:.2f}%")