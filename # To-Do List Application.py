# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("What task would you like to add? ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your to-do list!")

# Function to view tasks
def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty. Time to get productive!")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the number of the task you want to remove: ")) - 1
            if 0 <= task_number < len(tasks):
                removed_task = tasks.pop(task_number)
                print(f"Task '{removed_task}' has been successfully removed!")
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Your to-do list is already empty. Nothing to remove!")

# Main loop
while True:
    print("\nWelcome to Your To-Do List:")
    print("1. Add a Task")
    print("2. View Your Tasks")
    print("3. Remove a Task")
    print("4. Quit")
    choice = input("What would you like to do? ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Thank you for using your To-Do List. Have a productive day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
