# Calorie Tracker

# Data
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
    user_id = len(entries) + 1 # Used the length the list for this

    name = input("Enter your name: ")
    age = get_integer("Enter your age: ")
    weight = get_float("Enter your weight (kg): ")
    height = get_float("Enter your height (cm): ")
    
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


# Function to calculate BMI
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
            return bmi
        
    print("User ID not found")


# Main Menu 
def main_menu():
    print("Main Menu")
    print("1. Add personal information")
    print("2. View Personal information")
    print("3. Calculate BMI (Body Mass Index)") 
    print("4. Exit")

    option = get_integer("Select an option: ")

    if option == 1:
        add_entry()

    elif option == 2:
        display_entry()

    elif option == 3:
        calculate_and_display_bmi()     

    elif option == 4:
        print("Bye")
        return False
        
    else: 
        print("Enter a valid option")
            
    return True

# These lines ensure that the code runs properly
while main_menu():
    pass
    