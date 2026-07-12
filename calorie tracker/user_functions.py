from storage import entries, save_data
from input_helpers import get_integer, get_float, get_sex

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
            if data["name"].lower() == user_name.lower():
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
    height = get_float("Enter your height (cm): ")
    sex = get_sex()
    
    personal_information["id"] = user_id
    personal_information["name"] = name
    personal_information["age"] = age
    personal_information["weight"] = weight
    personal_information["height"] = height
    personal_information["sex"] = sex
    personal_information["weight_history"] = [] # For add_weight_record so a list of dictionaries becomes a value
    personal_information["calorie_history"] = []

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
        if key != "weight_history" and key != "calorie_history":
            print(key, value) 

    if "calorie_history" not in user:
        user["calorie_history"] = []

    print(f"Weight records: {len(user['weight_history'])}")
    print(f"Calorie records: {len(user['calorie_history'])}")
