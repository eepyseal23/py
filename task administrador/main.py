# RUN THE PROGRAM FROM THIS FILE
# Welcome to my personal life management
# My head renounced, so I had to do this to organize myself

import os

from input_helpers import get_integer
from storage import load_tasks

from task_functions import (
    add_task, 
    view_all_tasks, 
    mark_tasks_done, 
    delete_task, 
    view_pending_tasks, 
    view_done_tasks,
    search_task,
    view_tasks_due_today,
    edit_task
)

# Load all stored data
tasks = load_tasks()

# Main menu
def main_menu(tasks):
    os.system("cls")

    print("=" * 40)
    print("TASK ADMINISTRATOR")
    print("=" * 40)

    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. View pending tasks")
    print("6. View tasks that are done")
    print("7. Search task (keyword)")
    print("8. View tasks due today")
    print("9. Edit task")
    print("10. Exit")

    option = get_integer()

    if option == 1:
        add_task(tasks)

    elif option == 2:
        view_all_tasks(tasks)

    elif option == 3:
        mark_tasks_done(tasks)

    elif option == 4:
        delete_task(tasks)

    elif option == 5:
        view_pending_tasks(tasks)

    elif option == 6:
        view_done_tasks(tasks)

    elif option == 7:
        search_task(tasks)

    elif option == 8:
        view_tasks_due_today(tasks)

    elif option == 9:
        edit_task(tasks)

    elif option == 10:
        print("Bye")
        return False
    
    else:
        print("Enter a valid choice")

    input("\nPress Enter to return to the menu...")
    return True

# These lines ensure that the code runs properly
while main_menu(tasks):
    pass
