#RUN THE PROGRAM ON THIS FILE

from storage import load_data
from input_helpers import get_integer
from calorie_records import add_calorie_record

from user_functions import (
    add_entry,
    display_entry,
    display_single_entry,
    edit_entry,
    delete_entry
)

from health_calculations import (
    calculate_and_display_bmi,
    calculate_and_display_bmr,
    calculate_tdee,
    calorie_recommendations
)

from weight_records import (
    add_weight_record,
    display_weight_history,
    display_weight_stats,
    edit_weight_record,
    delete_weight_record
)

from calorie_records import (
    add_calorie_record,
    display_calorie_history,
    display_daily_calorie_stats,
    edit_calorie_record,
    delete_calorie_record
)
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
    print("13. Edit weight record")
    print("14. Delete weight record")
    print("15. Add calorie record")
    print("16. Exit")

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
        edit_weight_record()

    elif option == 14:
        delete_weight_record()

    elif option == 15:
        add_calorie_record()

    elif option == 16: 
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
    