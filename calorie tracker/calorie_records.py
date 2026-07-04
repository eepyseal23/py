from datetime import datetime

from storage import save_data
from input_helpers import get_integer, get_float
from user_functions import menu_for_choice_to_look_for_users


# Function to make sure the user has calorie history
def ensure_calorie_history(user):
    if "calorie_history" not in user:
        user["calorie_history"] = []


# Function to add calorie record
def add_calorie_record():
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