# Welcome to my Calorie Tracker
# Enjoy (I hope so)

# Modules and Global Variables
from datetime import datetime    # For the dates in weight records
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
        

# Function to get sex 
def get_sex():
    while True:
        sex = input("Enter biological sex (M/F): ").upper()

        if sex in ["M", "F"]:
            return sex

        print("Sex must be either M or F")


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
        print("Select an option: ")
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

    if not entries:
        user_id = 1    # If there are no users yet, start IDs at 1

    else:
        user_id = max(data["id"] for data in entries) + 1    # Otherwise, find the highest existing ID and add 1 (to prevent repeated ids)

    name = input("Enter your name: ")
    age = get_integer("Enter your age: ")
    weight = get_float("Enter your weight (kg): ")
    height = get_integer("Enter your height (cm): ")
    sex = get_sex()
    
    personal_information["id"] = user_id
    personal_information["name"] = name
    personal_information["age"] = age
    personal_information["weight"] = weight
    personal_information["height"] = height
    personal_information["sex"] = sex
    personal_information["weight_history"] = [] # For add_weight_record so a list of dictionaries becomes a value

    entries.append(personal_information)

    save_data()
    print("Added successfully")


# Function to edit a user's info
def edit_entry():
    if not entries:
        print("No users found")
        return

    user = menu_for_choice_to_look_for_users()

    print("1. Edit name")
    print("2. Edit age")
    print("3. Edit weight")
    print("4. Edit height")
    print("5. Edit sex")

    option = get_integer("Select an option: ")

    if option == 1:
        user["name"] = input("Enter new name: ")

    elif option == 2:
        user["age"] = get_integer("Enter new age: ")

    elif option == 3:
        user["weight"] = get_float("Enter new weight: ")

    elif option == 4:
        user["height"] = get_float("Enter new height: ")

    elif option == 5:
        user["sex"] = get_sex()

    else:
        print("Invalid option")
        return

    save_data()
    print("Data updated successfully")


# Function that deletes users
def delete_entry():
    if not entries:
        print("Nothing to delete")
        return 
    
    user = menu_for_choice_to_look_for_users()

    confirmation = input("Are you sure? (Y/N): ").upper()

    if confirmation != "Y":
        print("Deletion cancelled")
        return

    entries.remove(user)

    save_data()
    print("Deleted successfully")
    

# Function that displays data (everything)
def display_entry():
    if not entries:
        print("No entries found")
        return 

    for data in entries:
        print("---------------")
        for key, value in data.items():
            print(key, value)
        print("---------------")


# Function that displays data (single user)
def display_single_entry():
    if not entries:
        print("No entries found")
        return
    
    user = menu_for_choice_to_look_for_users()

    for key, value in user.items():
        if key != "weight_history":  # To avoid printing the long list of weights
            print(key, value)

    print(f"Weight records: {len(user['weight_history'])}")


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
    bmr = calculate_bmr(user)

    print("BMR:", round(bmr, 2))


# Function to calculate BMR (just to avoid repeating code)
def calculate_bmr(user):
    if user["sex"] == "M":
        return (10 * user["weight"]) + (6.25 * user["height"]) - (5 * user["age"]) + 5

    return (10 * user["weight"]) + (6.25 * user["height"]) - (5 * user["age"]) - 161


# This function calculates your TDEE (Total Daily Energy Expenditure)
def calculate_tdee():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    bmr = calculate_bmr(user)
 
    print("1. Sedentary")
    print("2. Light Exercise")
    print("3. Moderate")
    print("4. Active")
    print("5. Very Active")

    while True:
        option = get_integer("Select your level of physical actiity: ")

        if option == 1:
            tdee = bmr * 1.2
            break
    
        elif option == 2:
            tdee = bmr * 1.375
            break
    
        elif option == 3:
            tdee = bmr * 1.55
    
        elif option == 4:
            tdee = bmr * 1.725
            break
    
        elif option == 5:
            tdee = bmr * 1.9
            break
    
        print("Invalid choice")

    print(f"TDEE: {round(tdee, 2)} kcal")
    return tdee


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
        

# Function that displays weight stats (highest, lowest, current, gained/lost)
def display_weight_stats():

    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    print("User found")

    if not user["weight_history"]:
        print("This user has no weight history")
        return
    
    weights = [record["weight"] for record in user["weight_history"]]

    current_weight = user["weight"]
    highest_weight = max(weights)
    lowest_weight = min(weights)

    print(f"Current weight: {current_weight}")
    print(f"Highest weight: {highest_weight}")
    print(f"Lowest weight: {lowest_weight}")

    initial_weight = weights[0]
    weight_difference = current_weight - initial_weight
    
    if weight_difference < 0:
        print(f"Weight lost: {abs(weight_difference)} kg")
    
    elif weight_difference > 0:
        print(f"Weight gained: {weight_difference} kg")

    else:
        print("No weight difference")


# Funcion to provide recommendations based on your goals
def calorie_recommendations():
    tdee = calculate_tdee()

    maintenance = tdee
    mild_deficit = tdee - 250
    weight_loss = tdee - 500
    aggressive = tdee - 1000
    lean_bulk = tdee + 300

    print("Calorie Recommendations")
    print(f"Maintenance: {round(maintenance, 2)} kcal")
    print(f"Mild Deficit: {round(mild_deficit, 2)} kcal")
    print(f"Weight Loss: {round(weight_loss, 2)} kcal")
    print(f"Aggressive Cut: {round(aggressive, 2)} kcal")
    print(f"Lean Bulk: {round(lean_bulk, 2)} kcal")




# Main Menu 
def main_menu():
    print("Main Menu")
    print("1. Add personal information")
    print("2. View all info")
    print("3. View user's specific info ")
    print("4. Calculate BMI (Body Mass Index)") 
    print("5. Calculate BMR (Basal Metabolic Rate)")
    print("6. Calculate TDEE (Total Daily Energy Expenditure)")
    print("7. Add weight record")
    print("8. View weight history")
    print("9. Display weight stats")
    print("10. Edit entry")
    print("11. Delete entry")
    print("12. View calorie recommendetions")
    print("13. Exit")

    option = get_integer("Select an option: ")

    if option == 1:
        add_entry()

    elif option == 2:
        display_entry()

    elif option == 3:
        display_single_entry()

    elif option == 4:
        calculate_and_display_bmi()     
    
    elif option == 5:
        calculate_and_display_bmr()

    elif option == 6:
        calculate_tdee()

    elif option == 7:
        add_weight_record()

    elif option == 8:
        display_weight_history()

    elif option == 9:
        display_weight_stats()

    elif option == 10:
        edit_entry()

    elif option == 11:
        delete_entry()

    elif option == 12:
        calorie_recommendations()

    elif option == 13: 
        print("Bye")
        return False
        
    else: 
        print("Enter a valid option")
            
    return True

# Load data before running the code
load_data()    

# These lines ensure that the code runs properly
while main_menu():
    pass
    