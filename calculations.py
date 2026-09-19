def calculate_unserved_waste(prepared, served):
    return prepared - served

def calculate_total_waste(unserved_waste, estimated_plate_waste):
    return unserved_waste + estimated_plate_waste

def calculate_waste_percentage(total_waste, prepared):
    if prepared == 0:
        return 0

    return round((total_waste / prepared) * 100, 2)