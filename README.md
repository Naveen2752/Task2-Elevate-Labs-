# Task2-Elevate-Labs-
# ✅ Simple To-Do List Manager

A lightweight and beginner-friendly **Command Line To-Do List Manager** built using Python.  
It allows you to **add**, **view**, and **remove** tasks — all stored persistently in a local `todo.txt` file.

---

## 📌 Features

- Add new tasks  
- View all tasks with numbering  
- Remove tasks by index  
- Tasks are stored in a persistent `todo.txt` file  
- Graceful handling of missing files and invalid inputs  
- Simple and clean CLI interface  

---

## 🗂️ How It Works

This application uses basic **file I/O operations** to manage tasks.  
All logic is centered inside the `main()` function, which runs an interactive CLI loop.

### **Data Storage**

- All tasks are saved inside a file named **`todo.txt`**  
- Located in the same directory as the script  
- Each task is stored on a new line  
- The file ensures tasks persist even after closing the app  

---

## 🔁 Application Flow (`main()` Function)

The program runs inside a `while True` loop, presenting a menu until the user chooses to exit.

### **1️⃣ Add a Task**
- Prompts the user for a task description  
- Opens `todo.txt` in **append mode (`a`)**  
- Writes the new task followed by a newline  

### **2️⃣ View Tasks**
- Opens `todo.txt` in **read mode (`r`)**  
- Loads all tasks into a list  
- If no tasks exist, shows `"No tasks found"`  
- Displays each task with a numbered index (1, 2, 3...)  

### **3️⃣ Remove a Task**
- First displays the current tasks  
- Prompts for the task number to remove  
- Validates the input  
- Removes the chosen task using `list.pop()`  
- Rewrites all remaining tasks to `todo.txt` using **write mode (`w`)**  

### **4️⃣ Exit**
- Breaks the loop and ends the program gracefully  

---

## ⚠️ Error Handling

The app uses `try-except` blocks for:

- **FileNotFoundError**  
  When `todo.txt` is missing, the program handles it gracefully and creates it automatically when adding tasks.

- **ValueError**  
  Prevents crashes when users enter invalid menu options or non-numeric task numbers.

---

## 🛠️ Installation & Usage

### **Prerequisites**
- Python 3 installed

### **Run the Program**

Save your file as:
todo_app.py


Then run it in your terminal:

```bash
python todo_app.py
```

Follow the on-screen prompts to manage your tasks.

### **📄 Example Interaction**
```
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 1
Enter new task: Buy groceries
Task added!

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 2
1. Buy groceries
```

### **🤝 Contributing**

Feel free to fork this repository, make improvements, and submit pull requests.
