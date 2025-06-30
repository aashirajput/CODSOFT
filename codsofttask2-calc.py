import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Select a valid operation")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Creating main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.configure(bg="#f0f0f0")

# Heading
heading = tk.Label(root, text="Basic Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0")
heading.pack(pady=10)

# First number input
tk.Label(root, text="Enter First Number:", bg="#f0f0f0").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Second number input
tk.Label(root, text="Enter Second Number:", bg="#f0f0f0").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Dropdown for operation selection
tk.Label(root, text="Select Operation:", bg="#f0f0f0").pack()
operation_var = tk.StringVar()
operation_var.set("Addition")  # Default operation
operations_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operations_menu.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", padx=10, pady=5)
calculate_button.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_result.pack(pady=10)

# Run the application
root.mainloop()