# test_validation.py

from validation import validate_date, validate_positive_integer, validate_logical_constraints

def test_validate_date():
    """Test date validation."""
    assert validate_date("2025-09-20") == True
    assert validate_date("20-09-2025") == False
    assert validate_date("invalid") == False
    print("✓ Date validation tests passed")

def test_validate_positive_integer():
    """Test positive integer validation."""
    assert validate_positive_integer("100") == True
    assert validate_positive_integer("0") == True
    assert validate_positive_integer("-5") == False
    assert validate_positive_integer("abc") == False
    print("✓ Positive integer validation tests passed")

def test_validate_logical_constraints():
    """Test logical constraints validation."""
    # Valid case
    assert validate_logical_constraints(100, 95, 80) == True
    # served > prepared (invalid)
    assert validate_logical_constraints(100, 110, 80) == False
    # consumed > served (invalid)
    assert validate_logical_constraints(100, 95, 100) == False
    print("✓ Logical constraints validation tests passed")

if __name__ == "__main__":
    print("Running validation tests...\n")
    
    test_validate_date()
    test_validate_positive_integer()
    test_validate_logical_constraints()
    
    print("\nAll validation tests passed.")