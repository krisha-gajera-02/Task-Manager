tasks = []  # List to store tasks

def add_task():
    """Add a new task with a priority level and category."""
    user_task = input("Enter your task: ").strip()
    if user_task:
        # Set priority
        print("\nSet the priority for this task:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        try:
            priority_choice = int(input("Enter your choice (1/2/3): "))
            if priority_choice == 1:
                priority = "High"
            elif priority_choice == 2:
                priority = "Medium"
            elif priority_choice == 3:
                priority = "Low"
            else:
                print("Invalid choice! Defaulting priority to 'Medium'.")
                priority = "Medium"

            # Set category
            print("\nSet the category for this task:")
            print("1. Work")
            print("2. Personal")
            print("3. Urgent")
            category_choice = int(input("Enter your choice (1/2/3): "))
            if category_choice == 1:
                category = "Work"
            elif category_choice == 2:
                category = "Personal"
            elif category_choice == 3:
                category = "Urgent"
            else:
                print("Invalid choice! Defaulting category to 'Personal'.")
                category = "Personal"

            # Create task
            task = {
                "id": len(tasks) + 1,
                "name": user_task,
                "priority": priority,
                "category": category,
                "status": "pending"
            }
            tasks.append(task)
            print(f"Task added: {user_task} | Priority: {priority} | Category: {category}")
        except ValueError:
            print("Invalid input. Task not added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """View all tasks with their priorities and categories."""
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"Id: {task['id']} - Task: {task['name']} - Priority: {task['priority']} - Category: {task['category']} - Status: {task['status']}")
        
    else:
        print("\nNo tasks to display.")

def complete_task():
    """Mark a task as completed."""


    if not tasks:
        print("\nNo tasks to complete.")
        return
    
    try:
        view_tasks()
        
        task_id = int(input("Enter the task ID you have completed: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "completed":
                    print(f"Task is already completed: {task['name']}")
                else:
                    task["status"] = "completed"
                    print(f"Task completed: {task['name']}")
                break
        else:
            print("Task ID not found.")
    except ValueError:
        print("Please enter a valid task ID.")

def show_progress():
    """Display progress of completed tasks."""
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks to track progress.")
        return

    completed_tasks = sum(1 for task in tasks if task["status"] == "completed")
    progress = (completed_tasks / total_tasks) * 100
    print(f"\nProgress: {completed_tasks}/{total_tasks} tasks completed ({progress:.2f}%).")

def show_menu():
    """Display the menu."""
    print("\nWelcome to the Personal Task Manager")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Show progress")
    print("5. Exit")

def todo_app():
    """Run the to-do app."""
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                complete_task()
            elif choice == 4:
                show_progress()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

# call the function
todo_app()
