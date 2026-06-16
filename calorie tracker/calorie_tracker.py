# Calorie Tracker

# Modules and Global Variables
from datetime import datetime
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


# Function that handles data entry
def add_entry():
    personal_information = {}
    user_id = len(entries) + 1 # Used the length of the list for this

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
    personal_information["weight_history"] = [] # From add_weight_record so a list of dictionaries becomes a value

    entries.append(personal_information)


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
    
    user_id = get_integer("Enter the id of whose BMI you want to calculate: ")

    for data in entries:
        if data["id"] == user_id:
            height_in_meters = data["height"] / 100
            bmi = data["weight"] / height_in_meters ** 2
            print("BMI:", round(bmi, 2))
            return
        
    print("User ID not found")


# Function to calculate BMR (Basal Metabolic Rate)
def calculate_and_display_bmr():
    if not entries:
        print("No users found")
        return
    
    user_id = get_integer("Enter the id of whose BMR you want to calculate: ")

    for data in entries:
        if data["id"] == user_id:
            if data["sex"] == "M":
                bmr = (10 * data["weight"]) + (6.25 * data["height"]) - (5 * data["age"]) + 5
            else:
                bmr =  (10 * data["weight"]) + (6.25 * data["height"]) - (5 * data["age"]) - 161

            print("BMR:", round(bmr, 2))
            return

    print("User not found")


# Function to add weight record
def add_weight_record():
    weight_record = {}
    recorded_weight = get_float("Enter your weight in kg: ")

    while True:
        date_of_recorded_weight = input("Enter the date of your weight (DD/MM/YYYY)")

        try:
            datetime.strptime(date_of_recorded_weight, "%d/%m/%Y")
        except ValueError:
            print("Invalid date")
            continue

        print("Date added successfully")
        break

    weight_record["weight"] = recorded_weight
    weight_record["date"] = date_of_recorded_weight

    user_id = get_integer("Enter user ID: ")

    for data in entries:
        if data["id"] == user_id:
            data["weight_history"].append(weight_record)
            print("Weight record added successfully")
            return

    print("User ID not found")


# Main Menu 
def main_menu():
    print("Main Menu")
    print("1. Add personal information")
    print("2. View Personal information")
    print("3. Calculate BMI (Body Mass Index)") 
    print("4. Calculate BMR (Basal Metabolic Rate)")
    print("5. Add weight record")
    print("6. Exit")

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
        print("Bye")
        return False
        
    else: 
        print("Enter a valid option")
            
    return True

# These lines ensure that the code runs properly
while main_menu():
    pass
    