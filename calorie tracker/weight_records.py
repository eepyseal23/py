from datetime import datetime
from storage import entries, save_data
from input_helpers import get_integer, get_float
from user_functions import menu_for_choice_to_look_for_users

# Function to recalculate one's current weight
def update_current_weight(user):
    if not user["weight_history"]:
        return

    history = sorted(
        user["weight_history"],
        key=lambda record: datetime.strptime(record["date"], "%d/%m/%Y")
    )

    most_recent_record = history[-1]
    user["weight"] = most_recent_record["weight"]

# Function to add weight record
def add_weight_record():
    if not entries:
        print("No entries found")
        return
    
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

    update_current_weight(user)
    save_data()    # Save it

    print("Weight record added successfully")
    
# Function to edit weight records
def edit_weight_record():
    if not entries:
        print("No entries found")
        return
    
    user = menu_for_choice_to_look_for_users()

    if not user["weight_history"]:
        print("This user has no weight history")
        return
    
    for index, record in enumerate(user["weight_history"], start=1):
        print(f"{index}. {record['date']} - {record['weight']} {record['unit']}")

    option = get_integer("Enter your choice to update any record: ")

    if option > len(user["weight_history"]):
        print("Invalid option")
        return

    selected_record = user["weight_history"][option - 1]

    print("1. Edit weight")
    print("2. Edit date")

    edit_option = get_integer("Select what you want to edit: ")

    if edit_option == 1:
        selected_record["weight"] = get_float("Enter new weight in kg: ")

    elif edit_option == 2:
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

    update_current_weight(user)
    save_data()

    print("Weight record updated successfully")

# Function to delete one's weight record
def delete_weight_record():

    if not entries:
        print("No users found")
        return
    
    user = menu_for_choice_to_look_for_users()

    if not user["weight_history"]:
        print("This user has no weight history")
        return
    
    for index, record in enumerate(user["weight_history"], start=1):
        print(f"{index}. {record['date']} - {record['weight']} {record['unit']}")

    option = get_integer("Enter your choice to delete any record: ")

    if option > len(user["weight_history"]):
        print("Invalid option")
        return

    selected_record = user["weight_history"][option - 1]

    confirmation = input("Are you sure? (Y/N): ").upper()

    if confirmation != "Y":
        print("Deletion cancelled")
        return

    user["weight_history"].remove(selected_record)

    update_current_weight(user)
    save_data()

    print("Weight record deleted successfully")    

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
    average_weight = sum(weights) / len(weights)

    print(f"Current weight: {current_weight}")
    print(f"Highest weight: {highest_weight}")
    print(f"Lowest weight: {lowest_weight}")
    print(f"Average weight: {round(average_weight, 2)}")

    history = sorted(
        user["weight_history"],
        key=lambda record: datetime.strptime(record["date"], "%d/%m/%Y")
    )

    initial_weight = history[0]["weight"]
    weight_difference = current_weight - initial_weight
    
    if weight_difference < 0:
        print(f"Weight lost: {abs(weight_difference)} kg")
    
    elif weight_difference > 0:
        print(f"Weight gained: {weight_difference} kg")

    else:
        print("No weight difference")
        