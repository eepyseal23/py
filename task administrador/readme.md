# Task Administrator

A simple command-line task manager built with Python.

This project was created as a learning exercise to practice Python fundamentals such as functions, modules, JSON storage, input validation, lists, dictionaries, file handling, and project organization.

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Search tasks by keyword
- View pending tasks
- View completed tasks
- View tasks due today
- Persistent storage using JSON
- Input validation for dates, numbers, and empty fields

## Project Structure

```text
.
├── main.py
├── storage.py
├── task_functions.py
├── input_helpers.py
├── tasks.json
└── README.md
```

## Task Structure

Each task is stored as a dictionary inside a JSON file.

Example:

```json
{
    "task_title": "Finish Python project",
    "due_date": "15/07/2026",
    "additional_notes": "Push to GitHub",
    "status": "Pending"
}
```

## Requirements

- Python 3.10 or newer

No external libraries are required.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/eepyseal23/task-administrator.git
```

Move into the project folder:

```bash
cd task-administrator
```

Run the program:

```bash
python main.py
```

## Concepts Practiced

- Functions
- Parameters and return values
- Modules
- Imports
- Lists
- Dictionaries
- Nested data structures
- JSON serialization
- File handling
- Exception handling
- Input validation
- Loops
- CRUD operations
- Code refactoring

## Future Improvements

- Task priorities
- Categories
- Sorting by due date
- Automatic overdue detection
- Multiple users
- Colored terminal output
- Recurring tasks
- Export to CSV

## License

This project is intended for educational purposes.