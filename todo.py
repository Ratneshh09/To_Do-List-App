import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{idx}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("Enter a new task: ").strip()
    if task_name:
        tasks.append({'task': task_name, 'done': False})
        print("➕ Task added.")
    else:
        print("⚠️ Task name can't be empty.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            print("✅ Task marked as completed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again.")

if __name__ == "__main__":
    menu()
