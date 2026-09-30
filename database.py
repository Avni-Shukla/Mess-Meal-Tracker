# database.py
import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "mess_meal_tracker.db"


def get_connection() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    # Ensure data directory exists
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # so we can access columns by name
    return conn


def ensure_schema(conn: sqlite3.Connection):
    """Create the meal_records table if it does not exist."""
    sql = """
    CREATE TABLE IF NOT EXISTS meal_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT UNIQUE NOT NULL,
        meals_prepared INTEGER NOT NULL CHECK (meals_prepared >= 0),
        meals_served INTEGER NOT NULL CHECK (meals_served >= 0),
        meals_consumed INTEGER NOT NULL CHECK (meals_consumed >= 0),
        food_waste INTEGER NOT NULL CHECK (food_waste >= 0),
        CHECK (meals_served <= meals_prepared),
        CHECK (meals_consumed <= meals_served)
    );
    """
    conn.execute(sql)
    conn.commit()


def insert_meal_record(
    conn: sqlite3.Connection,
    date: str,
    meals_prepared: int,
    meals_served: int,
    meals_consumed: int,
    food_waste: int,
):
    """Insert a new meal record into the database."""
    sql = """
    INSERT INTO meal_records
      (date, meals_prepared, meals_served, meals_consumed, food_waste)
    VALUES (?, ?, ?, ?, ?);
    """
    conn.execute(
        sql,
        (date, meals_prepared, meals_served, meals_consumed, food_waste),
    )
    conn.commit()


def get_today_record(conn: sqlite3.Connection, today: str) -> dict | None:
    """
    Get the meal record for a specific date (e.g. today).
    Returns a dict-like row or None if not found.
    """
    sql = """
    SELECT date, meals_prepared, meals_served, meals_consumed, food_waste
    FROM meal_records
    WHERE date = ?;
    """
    cur = conn.execute(sql, (today,))
    row = cur.fetchone()
    if row is None:
        return None
    return dict(row)


def get_all_records(conn: sqlite3.Connection) -> list[dict]:
    """
    Get all meal records ordered by date ascending.
    Returns a list of dict-like rows.
    """
    sql = """
    SELECT date, meals_prepared, meals_served, meals_consumed, food_waste
    FROM meal_records
    ORDER BY date ASC;
    """
    cur = conn.execute(sql)
    rows = cur.fetchall()
    return [dict(r) for r in rows]