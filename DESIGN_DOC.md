# Mess Meal Tracker - System Design Document

# Introduction & Background

Hostel messes have a significant amount of food wastage on daily basis as they cook huge amounts of food for their students. The root cause of this problem is lack of digital tool for mess managers to enter and track their daily figures. Instead of using Excel sheets or other digital tools to log the number of meals served and food wasted, mess managers have to maintain this in registers manually. This results in difficulty to analyze trends in meal patterns and waste trends, which is critical in controlling costs and reducing food wastage.
This project, Mess Meal Tracker is a python utility that provides light-weight solution to this long-standing problem. It allows managers enter daily meal figures and calculate wastage automatically, thus saving lot of effort in manual calculations.

# Project Objectives

Following are objectives achieved while developing this project:

1. Creating a simplistic interface for entering prepared, served and consumed meals on daily basis.
2. Automatically calculate food-waste in terms of total number of wasted meals and meals percentage.
3. Storing entry records in a local file (persistent storage) for reference and analysis later.
4. Generating statistics about food-waste trends.
5. Creating an easy to use application that can be distributed widely as it has no third-party library requirements beyond standard python libraries.

# System Architecture & Technologies

## 3.1 Structural Overview
The code is developed using well defined layered approach. Following is a high-level architecture diagram showing components of this utility:
User Inputs ➔ Input Validations ➔ Math Calculations ➔ Database Operations
Further, configurations are managed separately and shared between components using config.py file.
The development approach kept files focused on specific features or functionalities. As a result, if a validation check fails, it's straight-forward to debug the issue in validation.py file without affecting other components such as database.py file. Similarly, database operations are isolated from calculations and user-interface code.

## 3.2 Technologies & Tools

Language: Python 3.10+
Database: SQLite 3 (using built-in sqlite3 module)
Code Editor: VS Code
Version Control: Git & GitHub
By using standard python modules only, the end-user can clone the repo and run python main.py right away without having to deal with virtual environments and pip install requirements.

# Functional Requirements

## 4.1 Features
### User Inputs:
i.Take entry date and meals prepared, meals served, meals consumed as input.
ii.Calculate total food-waste (meals prepared - meals consumed).
iii.Perform validation checks before writing entry to database.
### Queries:
i.Show today's entry (if any).
ii.Show all entries ordered by date.
iii.Show query results in form of tables in terminal.
### Database:
i.Store entry records in embedded database.
ii.Enforce validation rules at database level.

## 4.2 Entry Input Validation
Field Type Constraints:
Date: string (YYYY-MM-DD)
Meals Prepared: integer (>0)
Meals Served: integer (>0 and < meals prepared)
Meals Consumed: integer (>0 and < meals served)

# 5. Non-Functional Requirements & Design Decisions

## 5.1 Interface
A simple menu-based interface was designed keeping in mind users that are comfortable using terminal applications. It provides clear instruction about actions that can be taken. All user inputs are sanitized to prevent invalid entries. Further, appropriate feedback is provided when user enters invalid selections or input values.

## 5.2 Reliability
1.Database is saved on disk at data/mess_meal_tracker.db location. This helps avoid data-loss scenarios.
2.Database-level validations are implemented to ensure invalid records are not inserted into database.
3.Exception-handling blocks wrapped all user input reading and interrupt handling logic to avoid program exiting unexpectedly.

## 5.3 Code Organization
The code is organized in multiple files to follow separation of concerns principle. The code base is split into 7 key files as shown below:
File Description
main.py Entry-point and primary business logic.
database.py Manage relationships with underlying database.
calculations.py Mathematical operations.
validation.py Date-format validation and business rules.
views.py Manage appearance of command-line interface (CLI)
stats.py Statistical calculations.
test_validation.py Test-suite for testing validation logic.

# 6. Database Design
The database design is kept simple by using single table to store meal records. All constraints are enforced at application level to avoid invalid entries at database level. However, the table definition uses CHECK constraints to enforce rules whenever new records are inserted using INSERT statement.

## 6.1 Table Definition
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

## 6.2 Schema Overview
Field Notes
id Auto-incrementing field to store unique record identifier.
date Unique constraint ensures no duplicate entries for same date.
Constraints: Enforce business rules at database-level as secondary-layer of defense.

# 7. File Organization
mess-meal-tracker/
├── main.py
├── database.py
├── calculations.py
├── validation.py
├── config.py
├── views.py
├── stats.py
├── test_validation.py
├── README.md
├── DESIGN_DOC.md
└── data/
├── mess_meal_tracker.db

# 8. Testing

## 8.1 Unit Testing
Following unit tests ware written in test_validation.py file:
1.Test invalid date-strings such as 2026/09/30 or 30-09-2026 etc.
2.Test negative values such as -50.
3.Test edge-cases such as meals_served > meals_prepared etc.

## 8.2 Manual Testing
Following manual tests were performed:
1.Test duplicate entry by inserting same date twice and observing error-message.
2.Show empty query results when querying on fresh database file.
3.Test menu options for unexpected or invalid user selections.

# 9. Known Limitations
Some limitations are known in current version of Mess Meal Tracker:
1.The current version is command-line utility and doesn't have graphical interface.
2.The current version has no concept of user-logins or permissions.
3.The current version tracks total food-waste while tracking meals in general. It doesn't break-down entries for different meals (breakfast, lunch, dinner etc).