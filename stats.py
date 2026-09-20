# stats.py

import sqlite3
from config import DATABASE_PATH

def get_connection():
    """Get database connection."""
    return sqlite3.connect(DATABASE_PATH)

def calculate_average_waste():
    """Calculate average food waste across all records."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT AVG(food_waste) FROM meal_records")
    result = cursor.fetchone()[0]
    
    conn.close()
    
    if result is None:
        return 0
    return round(result, 2)

def get_total_waste():
    """Get total food waste across all records."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(food_waste) FROM meal_records")
    result = cursor.fetchone()[0]
    
    conn.close()
    
    if result is None:
        return 0
    return result

def get_total_records():
    """Get total number of records."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM meal_records")
    result = cursor.fetchone()[0]
    
    conn.close()
    
    return result

def display_statistics():
    """Display basic statistics."""
    print("\n" + "=" * 50)
    print("STATISTICS")
    print("=" * 50)
    print(f"Total Records: {get_total_records()}")
    print(f"Total Food Waste: {get_total_waste()} meals")
    print(f"Average Waste per Day: {calculate_average_waste()} meals")
    print("=" * 50)