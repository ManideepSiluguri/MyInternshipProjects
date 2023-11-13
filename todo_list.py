import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date=None, priority=None):
        task = {
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False,
        }
        self.tasks.append(task)

    def display_tasks(self):
        print("----- Tasks -----")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['description']} - Due Date: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']}")
        print("------------------")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            task['completed'] = True
            self.completed_tasks.append(task)
            print(f"Task '{task['description']}' marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description=None, due_date=None, priority=None):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            if description:
                task['description'] = description
            if due_date:
                task['due_date'] = due_date
            if priority:
                task['priority'] = priority
            print(f"Task {task_index} updated.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['description']}' removed.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting program.")
            break
        elif choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            priority = input("Enter priority (optional): ")
            todo_list.add_task(description, due_date, priority)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to update: "))
            description = input("Enter new description (press Enter to keep the same): ")
            due_date = input("Enter new due date (press Enter to keep the same): ")
            priority = input("Enter new priority (press Enter to keep the same): ")
            todo_list.update_task(task_index, description, due_date, priority)
        elif choice == '5':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main()
