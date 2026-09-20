# database.py

import sqlite3
from pathlib import Path
from config import DATABASE_PATH

def get_connection():
    """Get database connection."""
    Path("data").mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    """Initialize database and create table."""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        meals_prepared INTEGER NOT NULL,
        meals_served INTEGER NOT NULL,
        meals_consumed INTEGER NOT NULL,
        food_waste INTEGER NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()

def add_record(date, prepared, served, consumed, waste):
    """Add a meal record to the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO meal_records (date, meals_prepared, meals_served, meals_consumed, food_waste)
        VALUES (?, ?, ?, ?, ?)
    """, (date, prepared, served, consumed, waste))
    
    connection.commit()
    connection.close()

def get_today_record():
    """Get today's meal record."""
    from datetime import date
    connection = get_connection()
    cursor = connection.cursor()
    
    today = date.today().isoformat()
    
    cursor.execute("""
        SELECT id, date, meals_prepared, meals_served, meals_consumed, food_waste
        FROM meal_records
        WHERE date = ?
        ORDER BY id DESC
        LIMIT 1
    """, (today,))
    
    row = cursor.fetchone()
    connection.close()
    
    return row

def get_all_records():
    """Get all meal records."""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT id, date, meals_prepared, meals_served, meals_consumed, food_waste
        FROM meal_records
        ORDER BY date, id
    """)
    
    rows = cursor.fetchall()
    connection.close()
    
    return rows