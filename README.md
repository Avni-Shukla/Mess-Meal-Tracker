# Mess Meal Tracker

A simple command-line application to track daily meal quantities and food waste in a mess or hostel.

## Overview

Mess Meal Tracker helps mess managers and student coordinators record how many meals are prepared, served, and consumed each day. It automatically calculates food waste and stores all records in a SQLite database for future analysis.

## Features

- Add daily meal records (date, prepared, served, consumed)  
- Automatic calculation of food waste  
- Input validation (no negative numbers, logical constraints)  
- Persistent storage using SQLite  
- View today’s record  
- View all historical records  
- Modular, extensible codebase  
- Basic statistics (average waste, etc.)  

## Technologies / Tools Used

- Python 3  
- SQLite (via `sqlite3` module)  
- Standard library only (no external dependencies)  
- Git & GitHub for version control  

## Project Structure

```text
mess-meal-tracker/
├── main.py              # Entry point, user interface
├── database.py          # Database connection and CRUD operations
├── calculations.py      # Food waste calculations
├── validation.py        # Input validation functions
├── config.py            # Configuration constants
├── views.py             # Display and formatting functions
├── stats.py             # Basic statistics functions
├── test_validation.py   # Simple validation tests
├── statement.md         # Problem statement and scope
├── README.md            # This file
└── data/
    └── mess_meal_tracker.db  # SQLite database (created automatically)
```

## Installation & Running the Project

### Prerequisites

- Python 3 installed  
- Git installed (for cloning)  

### Steps

1. Clone the repository:

```bash
git clone [https://github.com/your-username/mess-meal-tracker.git](https://github.com/your-username/mess-meal-tracker.git)
cd mess-meal-tracker
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Run the application:

```bash
python main.py
```

The database (`data/mess_meal_tracker.db`) will be created automatically on first run.

## Instructions for Testing

### Manual Testing

1. Run `python main.py`  
2. Choose option `1` to add a meal record  
3. Enter sample data:
   - Date: `2025-09-20`  
   - Meals prepared: `100`  
   - Meals served: `95`  
   - Meals consumed: `80`  
4. Verify that waste is calculated correctly (`100 - 80 = 20`)  
5. Choose option `2` to view today’s record  
6. Choose option `3` to view all records  

### Automated Tests

Run the validation tests:

```bash
python test_validation.py
```

Expected output:

```text
Running validation tests...
All validation tests passed.
```

## Screenshots

(Add screenshots of:
- Main menu  
- Adding a meal record  
- Viewing records  
)

## License

This project is for educational purposes.