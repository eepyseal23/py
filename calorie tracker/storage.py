import json

entries = []    # This list contains everyone's info

# Functions
# Function to save data
def save_data():
    with open("users.json", "w") as file:
        json.dump(entries, file, indent = 4)

# Function to load data
def load_data():
    global entries

    try:
        with open("users.json", "r") as file:
            entries = json.load(file)    
    except FileNotFoundError:
        entries = []
    except json.JSONDecodeError: # Triggered when the file is found but it is corrupted
        entries = []
