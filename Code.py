import tkinter as tk  # Import tkinter library for creating GUI applications

# Global variable to store the current mathematical expression entered by the user
calculation = ""

def add_to_calculation(symbol):
    """
    Appends the clicked button's symbol (number/operator) to the ongoing calculation string.
    Prevents invalid input like multiple consecutive operators.
    """
    global calculation
    symbol = str(symbol)  # Ensure the symbol is treated as a string

    # Reset the calculation if the previous result was displayed
    if calculation == "Result":
        calculation = ""  # Start fresh for new input

    # Prevent entry of multiple consecutive operators like ++, --, **, etc.
    if calculation and calculation[-1] in "+-*/" and symbol in "+-*/":
        return  # Skip appending the operator

    # If already showing a result, overwrite with new symbol
    if calculation == "Result":
        calculation = symbol
    else:
        calculation += symbol  # Append the new symbol to the calculation

    # Update the display with the current calculation
    text_result.delete(1.0, "end")  # Clear existing content
    text_result.insert(1.0, calculation)  # Insert updated calculation

def evaluate_calculation():
    """
    Attempts to evaluate the current calculation using Python's eval().
    If successful, displays the result. If an error occurs, shows 'Error'.
    """
    global calculation
    try:
        result = str(eval(calculation))  # Evaluate the expression and convert to string
        calculation = result  # Store the result to allow chaining operations
        text_result.delete(1.0, "end")  # Clear the display
        text_result.insert(1.0, result)  # Show the result
    except:
        clear_field()  # Clear the input field in case of an exception
        text_result.insert(1.0, "Error")  # Display error message

def clear_field():
    """
    Clears both the stored calculation and the visual display.
    Triggered by pressing the 'C' (Clear) button.
    """
    global calculation
    calculation = ""  # Reset the calculation variable
    text_result.delete(1.0, "end")  # Clear text box

def on_enter(event):
    """
    Changes button appearance when the mouse hovers over it.
    Used for better user experience and feedback.
    """
    event.widget.config(bg="lightgray")  # Set hover color

def on_leave(event):
    """
    Resets button appearance when the mouse leaves it.
    """
    event.widget.config(bg="SystemButtonFace")  # Reset to default look

# Create the main application window
root = tk.Tk()  # Initialize tkinter window
root.geometry("350x300")  # Set fixed window size
root.title("Group 1 Calculator")  # Title shown in window bar

# Display area for showing calculation and results
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))  # Set up display field
text_result.grid(columnspan=5)  # Span across 5 columns to accommodate all buttons

# Create numeric buttons (0-9) and position them in a grid layout
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

# Operator buttons for basic math operations
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

# Parentheses for grouping expressions
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

# Clear button to reset calculator
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, bg="red", font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)  # Spans two columns

# Equals button to evaluate the current expression
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, bg="green", font=("Arial", 14))  
btn_equals.grid(row=6, column=3, columnspan=2)  # Spans two columns

# Run the application — main loop keeps window responsive and handles events
root.mainloop()
# End of the calculator program