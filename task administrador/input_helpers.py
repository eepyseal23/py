from datetime import datetime

# Function to get numbers to select options
def get_integer(prompt="Select a number: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Enter a number")

# Function to enter dates
def get_date():
    while True:
        date = input("Enter date (DD/MM/YYYY): ")

        try:
            datetime.strptime(date, "%d/%m/%Y")
            print("Date added successfully")
            return date
        except ValueError:
            print("Invalid date")

# Function to help with empty strings
def get_non_empty_string(prompt):
    while True:
        text = input(prompt).strip()

        if not text:
            print("This field cannot be empty")
            continue
    
        return text
