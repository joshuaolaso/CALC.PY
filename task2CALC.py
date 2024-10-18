import tkinter as tk

# Function to update the display when a button is pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(0, current + str(value))  # Append the clicked button's value

# Function to evaluate the expression in the entry field
def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(0, result)  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # Show error if evaluation fails

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.wm_colormapwindows
# Create an entry widget to display expressions and results
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()