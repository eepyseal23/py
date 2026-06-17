# Welcome to my Calorie Tracker
# Enjoy (I hope so)

# Modules and Global Variables
from datetime import datetime    # for the dates in weight records
import json    # To save data

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


# Function that gets integers when picking options and entering data
def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Enter a valid number")
        else:
            return number


# Function that gets decimals when entering data
def get_float(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Enter a valid number")
        else:
            return number


# Function used to search users by id
def get_user_by_id(prompt):
    while True:
        user_id = get_integer(prompt)

        for data in entries:
            if data["id"] == user_id:
                return data
                
        print("User not found")


# Function used to search by names
def get_user_by_name(prompt):
    while True:
        user_name = input(prompt)

        for data in entries:
            if data["name"] == user_name:
                return data
            
        print("User not found")


# A menu for the methods used to search for users either by name or by id                      
def menu_for_choice_to_look_for_users():

    while True:
        print('Select an option: ')
        print("1. Search user by ID")
        print("2. Search user by name")

        option = get_integer("Enter your choice: ")

        if option == 1:
            return get_user_by_id("Enter the id of the user: ")
        
        elif option == 2:
            return get_user_by_name("Enter the name of the user: ")
        
        print("Invalid choice")
    
       
# Function that handles data entry
def add_entry():
    personal_information = {}
    user_id = len(entries) + 1 # Used the length of the list "entries" for this

    name = input("Enter your name: ")
    age = get_integer("Enter your age: ")
    weight = get_float("Enter your weight (kg): ")
    height = get_integer("Enter your height (cm): ")
    
    while True:
        sex = input("Enter your biological sex (M/F)").upper() 

        if sex in ["M", "F"]:
            print("Added successfully")
            print("We ask for your biological sex to provide better results")
            break

        print("Sex must be either M or F")

    personal_information["id"] = user_id
    personal_information["name"] = name
    personal_information["age"] = age
    personal_information["weight"] = weight
    personal_information["height"] = height
    personal_information["sex"] = sex
    personal_information["weight_history"] = [] # For add_weight_record so a list of dictionaries becomes a value

    entries.append(personal_information)
    save_data()


# Function that displays data
def display_entry():
    if not entries:
        print("No entries found")
        return 

    for data in entries:
        print("---------------")
        for key, value in data.items():
            print(key, value)
        print("---------------")


# Function to calculate BMI (Body Mass Index)
def calculate_and_display_bmi():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()

    height_in_meters = user["height"] / 100
    bmi = user["weight"] / height_in_meters ** 2
    print("BMI:", round(bmi, 2))
    return
        

# Function to calculate BMR (Basal Metabolic Rate)
def calculate_and_display_bmr():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()

    if user["sex"] == "M":
        bmr = (10 * user["weight"]) + (6.25 * user["height"]) - (5 * user["age"]) + 5
    else:
        bmr =  (10 * user["weight"]) + (6.25 * user["height"]) - (5 * user["age"]) - 161

    print("BMR:", round(bmr, 2))
    return


# Function to add weight record
def add_weight_record():
    weight_record = {}
    recorded_weight = get_float("Enter your weight in kg: ")

    while True:
        date_of_recorded_weight = input("Enter the date of your weight (DD/MM/YYYY)")

        try:
            datetime.strptime(date_of_recorded_weight, "%d/%m/%Y")     # Tries to read the entered info as a valid date
        except ValueError:
            print("Invalid date")
            continue

        print("Date added successfully")
        break

    weight_record["weight"] = recorded_weight
    weight_record["unit"] = "kg"
    weight_record["date"] = date_of_recorded_weight

    user = menu_for_choice_to_look_for_users()

    user["weight_history"].append(weight_record)
    user["weight"] = recorded_weight   # Update weight in entries based on the user's entered info

    save_data()    # Save it

    print("Weight record added successfully")


# Function to display one's weight history 
def display_weight_history():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    print("User found")

    if not user["weight_history"]:
        print("This user has no weight history")
        return

    for user_info in user["weight_history"]:
        print("--------------------")
        for key, value in user_info.items():
            print(key, value)
        print("--------------------")
        

# Main Menu 
def main_menu():
    print("Main Menu")
    print("1. Add personal information")
    print("2. View personal information")
    print("3. Calculate BMI (Body Mass Index)") 
    print("4. Calculate BMR (Basal Metabolic Rate)")
    print("5. Add weight record")
    print("6. View weight history")
    print("7. Exit")

    option = get_integer("Select an option: ")

    if option == 1:
        add_entry()

    elif option == 2:
        display_entry()

    elif option == 3:
        calculate_and_display_bmi()     
    
    elif option == 4:
        calculate_and_display_bmr()

    elif option == 5:
        add_weight_record()

    elif option == 6:
        display_weight_history()

    elif option == 7: 
        print("Bye")
        return False
        
    else: 
        print("Enter a valid option")
            
    return True


# These lines ensure that the code runs properly
load_data()     # To load data before running the code

while main_menu():
    pass
    