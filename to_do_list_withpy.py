import tkinter as tk
from tkinter import messagebox

# --- Login Window ---
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        login_window.destroy()
        open_todo()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# --- To-Do List Window ---
def open_todo():
    todo = tk.Tk()
    todo.title("To-Do List")

    tasks = []

    def load_tasks():
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    tasks.append(line.strip())
                    listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

    def add_task():
        task = entry.get()
        if task != "":
            tasks.append(task)
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task():
        try:
            index = listbox.curselection()[0]
            tasks.pop(index)
            listbox.delete(index)
            save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def save_tasks():
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    entry = tk.Entry(todo, width=30)
    entry.pack(pady=10)

    tk.Button(todo, text="Add Task", command=add_task).pack()
    tk.Button(todo, text="Delete Task", command=delete_task).pack()

    listbox = tk.Listbox(todo, width=40, height=10)
    listbox.pack(pady=10)

    load_tasks()
    todo.mainloop()

# --- Main Login Window ---
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Username").grid(row=0, column=0)
entry_user = tk.Entry(login_window)
entry_user.grid(row=0, column=1)

tk.Label(login_window, text="Password").grid(row=1, column=0)
entry_pass = tk.Entry(login_window, show="*")
entry_pass.grid(row=1, column=1)

tk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2)

login_window.mainloop()
