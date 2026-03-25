# todo_manager.py

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")


while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")