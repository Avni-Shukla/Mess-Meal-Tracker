# Mess Meal Tracker - Project Statement

## Problem Statement

Messes and hostels often prepare more food than needed, leading to significant food waste. Without proper tracking of how much food is prepared, served, and actually consumed, it is difficult to identify patterns of waste or optimize meal planning.

## Scope of the Project

This project provides a simple command-line tool to track daily meal quantities in a mess:

- Record number of meals prepared, served, and consumed each day  
- Automatically calculate food waste  
- Store records persistently in a SQLite database  
- View today’s record or all historical records  

The system is designed as a minimal but complete example of a data-tracking application with validation, modular design, and basic statistics.

## Target Users

- Mess managers and hostel administrators  
- Student coordinators managing mess operations  
- Anyone interested in tracking and reducing food waste in group dining settings  

## High-Level Features

- Add daily meal records with date and quantities  
- Automatic calculation of food waste  
- Input validation (no negative numbers, logical constraints)  
- Persistent storage using SQLite  
- View today’s record or all records  
- Modular, extensible codebase with clear separation of concerns  
- Basic statistics on food waste (optional extension)  