# validation.py

from config import DATE_FORMAT

def validate_date(date_string):
    """Validate date format (YYYY-MM-DD)."""
    from datetime import datetime
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False

def validate_positive_integer(value):
    """Validate that value is a non-negative integer."""
    try:
        num = int(value)
        return num >= 0
    except ValueError:
        return False

def validate_logical_constraints(prepared, served, consumed):
    """Validate logical constraints between meal values."""
    if served > prepared:
        return False
    if consumed > served:
        return False
    return True

def validate_meal_values(prepared, served, plate_waste):
    """Legacy validation function."""
    if prepared <= 0:
        return False, "Prepared portions must be greater than 0."

    if served < 0:
        return False, "Served portions cannot be negative."

    if served > prepared:
        return False, "Served portions cannot be greater than prepared portions."

    if plate_waste < 0:
        return False, "Estimated plate waste cannot be negative."

    if plate_waste > served:
        return False, "Estimated plate waste cannot be greater than served portions."

    return True, "Valid input."