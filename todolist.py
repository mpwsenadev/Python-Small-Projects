class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if self.tasks:
            print("=" * 10)
            print("Task List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks in the list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task to be added: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to be removed: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
