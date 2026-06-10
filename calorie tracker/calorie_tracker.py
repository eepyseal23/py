# Calorie Tracker

# Data
entries = []

# Functions
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

    personal_information["age"] = age
    personal_information["weight"] = weight
    personal_information["height"] = height
    personal_information["sex"] = sex

    entries.append(personal_information)
    
# Function that displays data
def view_entry():
    print(entries)


# Main Menu 
def main_menu():
    print("Main Menu")
    print("1. Add personal information")
    print("2. View Personal information")
    print("3. Exit")

    option = get_integer("Select an option: ")

    if option == 1:
        add_entry()

    elif option == 2:
        view_entry()

    elif option == 3:
        print("Bye")
        return False
        
    else: 
        print("Enter a valid option")
            
    return True

# These lines ensure that the code runs properly
while main_menu():
    pass
    