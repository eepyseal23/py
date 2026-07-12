# Calorie Tracker

A Python console-based calorie and weight tracking application.

This project allows users to store personal information, track weight history, calculate health metrics, and manage daily calorie records. Data is saved locally using a JSON file.

## Features

- Add, view, edit, and delete users
- Save and load data using `users.json`
- Validate numeric inputs to prevent zero or negative values
- Handle missing or corrupted JSON files
- Calculate BMI
- Calculate BMR
- Calculate TDEE based on activity level
- Generate calorie recommendations
- Add weight records
- View weight history
- Edit and delete individual weight records
- Automatically update current weight based on the most recent weight record
- Add calorie records
- View calorie history
- Display daily calorie and protein totals
- Edit and delete individual calorie records

## Project Structure

```text
calorie_tracker/
│
├── main.py
├── storage.py
├── input_helpers.py
├── user_functions.py
├── health_calculations.py
├── weight_records.py
├── calorie_records.py
└── users.json
```

## File Overview

### `main.py`

Contains the main menu and runs the program.

### `storage.py`

Handles saving and loading data from `users.json`.

### `input_helpers.py`

Contains reusable input validation functions.

### `user_functions.py`

Handles user creation, editing, deletion, searching, and display.

### `health_calculations.py`

Contains BMI, BMR, TDEE, and calorie recommendation functions.

### `weight_records.py`

Handles weight history, weight stats, and editing/deleting weight records.

### `calorie_records.py`

Handles calorie history, daily calorie stats, and editing/deleting calorie records.

## How to Run

Make sure Python is installed.

Then run:

```bash
python main.py
```

## Data Storage

The program stores user data in a local JSON file called:

```text
users.json
```

Each user can have:

- Personal information
- Weight history
- Calorie history

Example user structure:

```json
{
    "id": 1,
    "name": "Juan",
    "age": 19,
    "weight": 85.0,
    "height": 173.0,
    "sex": "M",
    "weight_history": [],
    "calorie_history": []
}
```

## What I Learned

This project helped me practice:

- Python functions
- Lists and dictionaries
- JSON file handling
- Input validation
- Error handling
- Modular programming
- Imports between files
- CRUD operations
- Working with dates using `datetime`
- Building a console-based application

## Future Improvements

Possible improvements include:

- Add daily calorie goals
- Add protein goals
- Add weekly calorie and protein summaries
- Improve formatting for displayed data
- Prevent empty food names or user names
- Add support for pounds and inches
- Move from JSON storage to SQLite or PostgreSQL
- Add a graphical interface or web API

## Status

This is a beginner Python project built to practice core programming concepts and project organization.