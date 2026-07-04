from storage import entries
from input_helpers import get_integer
from user_functions import menu_for_choice_to_look_for_users

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
            break
    
        elif option == 4:
            tdee = bmr * 1.725
            break
    
        elif option == 5:
            tdee = bmr * 1.9
            break
    
        print("Invalid choice")

    print(f"TDEE: {round(tdee, 2)} kcal")
    return tdee

# Funcion to provide recommendations based on your goals
def calorie_recommendations():
    tdee = calculate_tdee()

    if tdee is None:
        return

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
