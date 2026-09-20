# calculations.py

def calculate_unserved_waste(prepared, served):
    """Calculate unserved waste (prepared - served)."""
    return prepared - served

def calculate_total_waste(unserved_waste, estimated_plate_waste):
    """Calculate total waste including plate waste."""
    return unserved_waste + estimated_plate_waste

def calculate_waste_percentage(total_waste, prepared):
    """Calculate waste percentage."""
    if prepared == 0:
        return 0
    return round((total_waste / prepared) * 100, 2)

def calculate_waste(prepared, consumed):
    """Calculate food waste (prepared - consumed)."""
    return prepared - consumed