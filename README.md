# Mess Meal Tracker

This is a command-line application used to track the daily mess meals. It is used to record the data and calculate the amount of wasted food in a mess or a hostel.

## Overview

Mess Meal Tracker can help the mess committee or the student body track the number of meals prepared, served, and consumed by the students every day. It can collect the data about the wasted food and save it in a SQLite database for later statistical analysis.

## Features

- Tracking and recording the meals - prepared, served, and consumed.
- Calculation of the wasted food.
- Validation of the user input.
- Storage of the recorded data in a SQLite database.
- Displaying of the data - today's record, all records.
- Easy to extend, modularized code
- Statistics collecting

## Technologies / Tools Used
- Python 3
- SQLite (for the database)
- The standard library modules
- Git and GitHub (for commits and version control)
The following tools and technologies have been used for the development of this project:

## Project Structure

├── main.py      # The main file containing the interface
├── database.py    # Database related operations
├── calculations.py  # Calculation related functions
├── validation.py   # Validation related functions
├── config.py     # The configuration file
├── views.py     # Views related functionality
├── stats.py     # Statistics related functionality
├── test_validation.py # Test cases for our validation function
├── statement.md   # Statement file
├── README.md     # This file
└── data/
└── mess_meal_tracker.db # The SQLite database

## Installation and Running the Project
The following prerequisites must be met in order to install and run the project locally on your machine:
- Python 3
- Git
Once the prerequisites are installed, run the following commands:

git clone [https://github.com/your-username/mess-meal-tracker.git](https://github.com/your-username/mess-meal-tracker.git)
cd mess-meal-tracker

If you'd like, you can create a virtual environment:
python -m venv venv
# activate the environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
Finally, run the program: python main.py
The database file (SQLite) will be created in the first run.

## Instructions for Testing

### Manual Testing
1. Run the program by typing `python main.py` in the terminal
2. Follow the instructions in the terminal
3. For testing choose the option `1` to add a record and enter the following data:
- Date: `2025-09-20`
- Meals prepared: `100`
- Meals served: `95`
- Meals consumed: `80`
The program will display the amount of wasted food (in this case it should be `100 - 80 = 20`). Follow the other options to view the data.

### Automated Testing
To run the automated tests, execute the following command: python test_validation.py
The following output should be displayed:
Running validation tests...
All validation tests passed.

## Screenshots
- Main menu 
- Add record
- View records

## License
This project is meant for educational purposes.