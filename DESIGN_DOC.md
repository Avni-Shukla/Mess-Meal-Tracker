# Mess Meal Tracker - Design Document

## 1. Problem Statement

Messes and hostels often prepare more food than needed, leading to significant food waste. Without proper tracking of how much food is prepared, served, and actually consumed, it is difficult to identify patterns of waste or optimize meal planning.

## 2. Objectives

- Track daily meal quantities (prepared, served, consumed)
- Calculate and record food waste automatically
- Store records persistently in a SQLite database
- Provide basic statistics on food waste patterns
- Help mess management make data-driven decisions to reduce waste

## 3. Functional Requirements

### 3.1 Major Functional Modules

**Module 1: Data Input & Processing**
- Add daily meal records with date, meals prepared, served, and consumed
- Automatic calculation of food waste (prepared - consumed)
- Input validation for all fields

**Module 2: CRUD Operations**
- Create: Add new meal records to database
- Read: View today's record or all historical records
- Database operations using SQLite

**Module 3: Reporting & Analytics**
- View today's meal record
- View all historical records
- Calculate statistics (total waste, average waste, total records)

### 3.2 Input/Output Structure

**Input:**
- Date: String (YYYY-MM-DD)
- Meals Prepared: Integer (≥ 0)
- Meals Served: Integer (≥ 0, ≤ prepared)
- Meals Consumed: Integer (≥ 0, ≤ served)

**Output:**
- Calculated food waste
- Stored record in database
- Display of records in formatted text

### 3.3 Logical Workflow

User selects option from main menu → Add Record / View Today / View All / Exit

## 4. Non-Functional Requirements

**4.1 Usability**
- Simple command-line interface with clear prompts
- Minimal learning curve for new users
- Clear error messages for invalid input

**4.2 Reliability**
- Persistent storage using SQLite database
- Data integrity through validation constraints
- Consistent date handling and formatting

**4.3 Error Handling Strategy**
- Input validation before processing
- Try-except blocks for exception handling
- Descriptive error messages for user guidance
- Graceful exit on critical errors

**4.4 Maintainability**
- Modular code structure (8 separate Python files)
- Clear function names and single responsibility
- Easy to extend with new features
- Configuration separated in config.py

**4.5 Resource Efficiency**
- Lightweight SQLite database (no external server)
- Standard library only (no external dependencies)
- Minimal memory footprint
- Efficient database queries

## 5. System Architecture

main.py (User Interface) → validation.py → calculations.py → database.py → SQLite DB
config.py provides configuration to all modules

## 6. Process Flow

1. Initialize Database
2. Show Main Menu
3. User selects option (1-4)
4. If Add Record: Input data → Validate → Calculate waste → Save to DB → Return to menu
5. If View Today: Query database → Display record → Return to menu
6. If View All: Query database → Display all records → Return to menu
7. If Exit: End program

## 7. UML Diagrams

**Use Case:** Mess Admin → Add Meal Record, View Today's Record, View All Records, View Statistics

**Components:** main.py, validation.py, calculations.py, database.py, config.py, views.py, stats.py, SQLite DB

**Sequence (Add Meal):** User → main.py (get input) → validation.py (validate) → calculations.py (calculate waste) → database.py (save) → SQLite (INSERT)

## 8. Database Design

**Table: meal_records**

Columns:
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- date (TEXT, NOT NULL)
- meals_prepared (INTEGER, NOT NULL)
- meals_served (INTEGER, NOT NULL)
- meals_consumed (INTEGER, NOT NULL)
- food_waste (INTEGER, NOT NULL)

**Schema:**
```sql
CREATE TABLE IF NOT EXISTS meal_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    meals_prepared INTEGER NOT NULL,
    meals_served INTEGER NOT NULL,
    meals_consumed INTEGER NOT NULL,
    food_waste INTEGER NOT NULL
);
```

**Constraints:**
- id: Auto-incrementing primary key
- date: NOT NULL, format YYYY-MM-DD
- meals_prepared: NOT NULL, ≥ 0
- meals_served: NOT NULL, ≥ 0, ≤ meals_prepared
- meals_consumed: NOT NULL, ≥ 0, ≤ meals_served
- food_waste: NOT NULL, calculated as (meals_prepared - meals_consumed)

## 9. Project Structure

mess-meal-tracker/
- main.py (Entry point, user interface)
- database.py (Database connection and CRUD operations)
- calculations.py (Food waste calculations)
- validation.py (Input validation functions)
- config.py (Configuration constants)
- views.py (Display and formatting functions)
- stats.py (Basic statistics functions)
- test_validation.py (Simple validation tests)
- statement.md (Problem statement and scope)
- README.md (Installation and usage guide)
- DESIGN_DOC.md (This design document)
- data/ (Folder for database)

## 10. Testing Strategy

**Unit Tests:**
- Date validation tests
- Positive integer validation tests
- Logical constraints validation tests

**Manual Testing:**
- Add meal record with valid data
- Add meal record with invalid data
- View today's record (with and without data)
- View all records (with and without data)
- Exit functionality

**Test Execution:**
```bash
python test_validation.py
python main.py
```

## 11. Technologies Used

- Language: Python 3
- Database: SQLite (via sqlite3 module)
- Version Control: Git & GitHub
- Dependencies: Standard library only (no external packages)

## 12. Future Enhancements

- Add meal type (breakfast, lunch, dinner)
- Graphical user interface (GUI)
- Export data to CSV/Excel
- Advanced analytics and visualizations
- Multi-user support
- Web-based interface