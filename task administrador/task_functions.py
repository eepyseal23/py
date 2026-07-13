from storage import save_tasks
from input_helpers import get_date, get_integer, get_non_empty_string
from datetime import datetime

#Function to add tasks
def add_task(tasks):
    new_task = {}

    task_title = get_non_empty_string("Enter task title: ")
    due_date = get_date()
    additional_notes = input("Enter additional notes, if not needed, press enter: ")

    new_task["task_title"] = task_title
    new_task["due_date"] = due_date
    new_task["additional_notes"] = additional_notes
    new_task["status"] = "Pending"

    tasks.append(new_task)

    save_tasks(tasks)
    print("Task added successfully")

# Function to display one task
def display_task(index, task):
    print(f"{index}. {task['task_title']}")
    print(f"Due date: {task['due_date']}")
    print(f"Additional notes: {task['additional_notes']}")
    print(f"Status: {task['status']}")
    print()

# Function to view/display tasks (all of them)
def view_all_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    for index, task in enumerate(tasks, start=1):
        display_task(index, task)

# Function to mark tasks as done
def mark_tasks_done(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    view_all_tasks(tasks)

    option = get_integer("Select the task number to mark as done: ")
    index = option - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return 
    
    if tasks[index]['status'] == "Done":
        print("This task is already done")
        return

    tasks[index]['status'] = "Done"
    save_tasks(tasks)
    print("Status updated successfully")

# Function to delete tasks
def delete_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    view_all_tasks(tasks)

    option = get_integer("Select the task number to be deleted: ")
    index = option - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    
    choice = input("Are you sure you want to delete this task? (Y/N): ").strip().upper()
    if choice == "Y":
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully")
    
    elif choice == "N":
        print("Deletion cancelled")
        return
    
    else:
        print("Invalid choice")
        return 

# Function that only displays tasks that are pending
def view_pending_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    found_pending = False

    for index, task in enumerate(tasks, start=1):
        if task['status'] == "Pending":
            found_pending = True
            display_task(index, task)

    if not found_pending:
        print("No pending tasks found")
        
# Function that only displays tasks that are done
def view_done_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    found_done = False

    for index, task in enumerate(tasks, start=1):
        if task['status'] == "Done":
            found_done = True
            display_task(index, task)

    if not found_done:
        print("No tasks that are done were found")
    
# Function to search tasks based on keywords appearing either on the task's name or in their notes
def search_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    keyword = get_non_empty_string("Enter a word to look for a task based on its name or notes: ").lower()
    found_task = False

    for index, task in enumerate(tasks, start=1):
        title = task['task_title'].lower()
        notes = task['additional_notes'].lower()

        if keyword in title or keyword in notes:
            found_task = True
            display_task(index, task)

    if not found_task:
        print("No matching tasks found")

# Function to see which tasks are due today
def view_tasks_due_today(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    today = datetime.today().strftime("%d/%m/%Y")
    found_today = False

    for index, task in enumerate(tasks, start=1):
        if task['due_date'] == today and task['status'] == "Pending":
            found_today = True
            display_task(index, task)

    if not found_today:
        print("No tasks due today")

# Function to edit tasks
def edit_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    view_all_tasks(tasks)

    chosen_task = get_integer("Select the task number to be edited: ")
    index = chosen_task - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    
    print("1. Edit task name")
    print("2. Edit task due date")
    print("3. Edit notes")
    print("4. Edit status")
    print("5. Cancel")

    option = get_integer("Select what you want to edit: ")

    if option == 1:
        new_title = get_non_empty_string("Enter a new task title: ")
        tasks[index]['task_title'] = new_title
  
    elif option == 2:
        new_date = get_date()
        tasks[index]['due_date'] = new_date

    elif option == 3:
        new_notes = input("Enter new notes: ")
        tasks[index]['additional_notes'] = new_notes

    elif option == 4:
        new_status = input("Enter new status (Pending/Done): ").strip().capitalize()

        if new_status not in ["Pending", "Done"]:
            print("Enter a valid status")
            return
 
        tasks[index]['status'] = new_status

    elif option == 5:
        print("Cancelled successfully")
        return

    else:
        print("Select a valid option")
        return

    save_tasks(tasks)
    print("Data saved successfully")

            








