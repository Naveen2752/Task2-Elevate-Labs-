def main():
    print("\n===== To Do List =====")
    while True:
        print("\nSelect an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                task = input("Enter the task to add: ")
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
                print(f'Task "{task}" added to the list.')

            elif choice == '2':
                print("\nYour To Do List:")
                try:
                    with open("todo.txt", "r") as file:
                        tasks = file.readlines()
                        if not tasks:
                            print("No tasks found.")
                        else:
                            for idx, task in enumerate(tasks, start=1):
                                print(f"{idx}. {task.strip()}")
                except FileNotFoundError:
                    print("No tasks found.")

            elif choice == '3':
                try:
                    with open("todo.txt", "r") as file:
                        tasks = file.readlines()
                        if not tasks:
                            print("No tasks to remove.")
                            continue

                    print("\nYour To Do List:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task.strip()}")

                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        with open("todo.txt", "w") as file:
                            file.writelines(tasks)
                        print(f'Task "{removed_task.strip()}" removed from the list.')
                    else:
                        print("Invalid task number.")
                except FileNotFoundError:
                    print("No tasks to remove.")


            elif choice == '4':
                print("Exiting the To Do List application. Goodbye!")
                break

            else:
                print("Invalid choice! Please select a valid option (1-4).")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
