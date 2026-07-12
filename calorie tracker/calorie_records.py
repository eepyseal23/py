from datetime import datetime

from storage import entries, save_data
from input_helpers import get_integer, get_float
from user_functions import menu_for_choice_to_look_for_users

# Function to make sure the user has calorie history
def ensure_calorie_history(user):
    if "calorie_history" not in user:
        user["calorie_history"] = []

# Function to add calorie record
def add_calorie_record():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    ensure_calorie_history(user)

    calorie_record = {}

    food_name = input("Enter food name: ")
    calories = get_integer("Enter calories: ")
    protein = get_float("Enter protein in grams: ")

    while True:
        date_of_food = input("Enter the date (DD/MM/YYYY): ")

        try:
            datetime.strptime(date_of_food, "%d/%m/%Y")
        except ValueError:
            print("Invalid date")
            continue

        print("Date added successfully")
        break

    calorie_record["food"] = food_name
    calorie_record["calories"] = calories
    calorie_record["protein"] = protein
    calorie_record["date"] = date_of_food

    user["calorie_history"].append(calorie_record)

    save_data()

    print("Calorie record added successfully")

# Function to display calorie history 
def display_calorie_history():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    ensure_calorie_history(user)

    if not user["calorie_history"]:
        print("This user has no calorie history")
        return
    
    for index, record in enumerate(user["calorie_history"], start=1):
        print(f"{index}. {record['date']} - {record['food']} - {record['calories']} kcal - {record['protein']}g protein")

# Function to display daily calorie stats
def display_daily_calorie_stats():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    ensure_calorie_history(user)

    if not user["calorie_history"]:
        print("This user has no calorie history")
        return

    while True:
        selected_date = input("Enter the date (DD/MM/YYYY): ")

        try:
            datetime.strptime(selected_date, "%d/%m/%Y")
        except ValueError:
            print("Invalid date")
            continue

        break

    daily_records = []

    for record in user["calorie_history"]:
        if record["date"] == selected_date:
            daily_records.append(record)

    if not daily_records:
        print("No calorie records found for this date")
        return

    total_calories = sum(record["calories"] for record in daily_records)
    total_protein = sum(record["protein"] for record in daily_records)

    print(f"Calorie stats for {selected_date}")
    print(f"Total calories: {total_calories} kcal")
    print(f"Total protein: {round(total_protein, 2)}g")

    print("Records:")
    for index, record in enumerate(daily_records, start=1):
        print(f"{index}. {record['food']} - {record['calories']} kcal - {record['protein']}g protein")

# Function to edit calorie records
def edit_calorie_record():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    ensure_calorie_history(user)

    if not user["calorie_history"]:
        print("This user has no calorie history")
        return
    
    for index, record in enumerate(user["calorie_history"], start=1):
        print(f"{index}. {record['date']} - {record['food']} - {record['calories']} kcal - {record['protein']}g protein")

    option = get_integer("Enter your choice to update any record: ")

    if option > len(user["calorie_history"]):
        print("Invalid option")
        return
    
    selected_record = user["calorie_history"][option - 1]

    print("1. Edit food name")
    print("2. Edit calories")
    print("3. Edit protein")
    print("4. Edit date")

    edit_option = get_integer("Select what you want to edit: ")

    if edit_option == 1:
        selected_record["food"] = input("Enter new food name: ")

    elif edit_option == 2:
        selected_record["calories"] = get_integer("Enter new calories: ")

    elif edit_option == 3:
        selected_record["protein"] = get_float("Enter new protein in grams: ")

    elif edit_option == 4:
        while True:
            new_date = input("Enter new date (DD/MM/YYYY): ")

            try:
                datetime.strptime(new_date, "%d/%m/%Y")
            except ValueError:
                print("Invalid date")
                continue

            selected_record["date"] = new_date
            break

    else:
        print("Invalid option")
        return
    
    save_data()
    print("Calorie record updated successfully")

# Function to delete calorie records
def delete_calorie_record():
    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()
    ensure_calorie_history(user)

    if not user["calorie_history"]:
        print("This user has no calorie history")
        return
    
    for index, record in enumerate(user["calorie_history"], start=1):
        print(f"{index}. {record['date']} - {record['food']} - {record['calories']} kcal - {record['protein']}g protein")

    option = get_integer("Enter your choice to delete any record: ")

    if option > len(user["calorie_history"]):
        print("Invalid option")
        return
    
    selected_record = user["calorie_history"][option - 1]

    confirmation = input("Are you sure? (Y/N): ").upper()

    if confirmation != "Y":
        print("Deletion cancelled")
        return
    
    user["calorie_history"].remove(selected_record)

    save_data()
    print("Calorie record deleted successfully")



        
