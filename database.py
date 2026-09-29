#database.py - Database operations for Mess Meal Tracker

import sqlite3
import os
from config import DATABASE_PATH

def get_connection():
    """Establish and return connection to SQLite database."""
    # Ensure data folder exists if specified in path
    db_dir = os.path.dirname(DATABASE_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)

# create meal record tables

def initialize_database():
    """Create meal_records table if it does not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meal_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL,
            meals_prepared INTEGER NOT NULL CHECK (meals_prepared >= 0),
            meals_served INTEGER NOT NULL CHECK (meals_served >= 0),
            meals_consumed INTEGER NOT NULL CHECK (meals_consumed >= 0),
            food_waste INTEGER NOT NULL CHECK (food_waste >= 0),
            CHECK (meals_served <= meals_prepared),
            CHECK (meals_consumed <= meals_served)
        )
    """)
    conn.commit()
    conn.close()

# Add Records

def add_record(date, prepared, served, consumed, waste):
    """Insert a new daily meal record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO meal_records (date, meals_prepared, meals_served, meals_consumed, food_waste)
        VALUES (?, ?, ?, ?, ?)
    """, (date, prepared, served, consumed, waste))
    conn.commit()
    conn.close()

# Get Today's records

def get_today_record(today_date):
    """Fetch record for a specific date."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, meals_prepared, meals_served, meals_consumed, food_waste 
        FROM meal_records 
        WHERE date = ?
    """, (today_date,))
    record = cursor.fetchone()
    conn.close()
    return record

# Get All Records

def get_all_records():
    """Fetch all historical meal records ordered by date."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, meals_prepared, meals_served, meals_consumed, food_waste 
        FROM meal_records 
        ORDER BY date ASC
    """)
    records = cursor.fetchall()
    conn.close()
    return records