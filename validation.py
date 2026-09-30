# validation.py
from datetime import datetime


def validate_date(date_str: str) -> str:
    """
    Validate date string in YYYY-MM-DD format.
    Raises ValueError if format is invalid.
    """
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    # Optional: reject future dates (agar chaho toh uncomment kar do)
    # if dt.date() > datetime.today().date():
    #     raise ValueError("Date cannot be in the future.")
    
    return date_str


def validate_meals(prepared: int, served: int, consumed: int) -> dict:
    """
    Validate meal counts according to business rules:
      - meals_prepared > 0
      - 0 < meals_served <= meals_prepared
      - 0 < meals_consumed <= meals_served
    
    Returns a dict with validated values and computed food_waste.
    Raises ValueError if any rule is violated.
    """
    if prepared <= 0:
        raise ValueError("meals_prepared must be greater than 0.")
    
    if not (0 < served <= prepared):
        raise ValueError("meals_served must be > 0 and <= meals_prepared.")
    
    if not (0 < consumed <= served):
        raise ValueError("meals_consumed must be > 0 and <= meals_served.")
    
    food_waste = prepared - consumed
    if food_waste < 0:
        raise ValueError("food_waste cannot be negative.")
    
    return {
        "meals_prepared": prepared,
        "meals_served": served,
        "meals_consumed": consumed,
        "food_waste": food_waste,
    }