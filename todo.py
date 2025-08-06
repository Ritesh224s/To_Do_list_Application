import os

TASKS_FILE = "tasks.txt"

# ---------------- Core Functions ---------------- #

def load_tasks():
    """Load tasks from the file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def save_tasks(tasks):
    """Save tasks from the list into the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    """Display current tasks."""
    if not tasks:
        print("\n📝 Your to-do list is empty.")
    else:
        print("\n📝 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Task cannot be empty.")

def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"❌ Task removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def clear_tasks(tasks):
    """Clear all tasks."""
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        tasks.clear()
        print("🗑️ All tasks cleared.")
    else:
        print("✅ Clear operation cancelled.")

def mark_complete(tasks):
    """Mark a task as completed by adding '[Done]' tag."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " [Done]"
            print(f"✅ Task marked as done: {tasks[task_num - 1]}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# ---------------- Main Program ---------------- #

def main():
    print("📋 Welcome to the Console To-Do List App")
    tasks = load_tasks()

    while True:
        print("\n--- Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            clear_tasks(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
