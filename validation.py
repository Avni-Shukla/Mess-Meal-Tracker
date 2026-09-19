def validate_meal_values(prepared, served, plate_waste):
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