# Simple To-Do List Application using Python Tkinter


import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task.strip() != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_task_count()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid task!")

# Function to delete selected task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
        update_task_count()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

#Function to mark task as completed
def mark_task_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(tk.END, task + " (Done)")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

# Function to clear all tasks
def clear_all_tasks():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)
        update_task_count()

# Function to update the task count label
def update_task_count():
    total_tasks = task_listbox.size()
    task_count_label.config(text=f"Total Tasks: {total_tasks}")

# Create main application window
root = tk.Tk()
root.title("My To-Do List App")
root.geometry("400x500")
root.config(bg="#f0f0f0")


# Title Label
title_label = tk.Label(root, text=" My Daily To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Entry for task input
task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text=" Add Task", width=15, bg="#add8e6", command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text=" Delete Task", width=15, bg="#ff7f7f", command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

done_button = tk.Button(button_frame, text=" Mark Done", width=15, bg="#90ee90", command=mark_task_done)
done_button.grid(row=0, column=1, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear All", width=15, bg="#ffa07a", command=clear_all_tasks)
clear_button.grid(row=1, column=1, padx=5, pady=5)
# Listbox to show tasks
task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10, selectbackground="#a0a0a0")
task_listbox.pack(pady=10)

# Task count label
task_count_label = tk.Label(root, text="Total Tasks: 0", font=("Arial", 10), bg="#f0f0f0")
task_count_label.pack()

# Run the Tkinter event loop
root.mainloop()