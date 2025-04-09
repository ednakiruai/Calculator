def evaluate_calculation():
    """Evaluates the current calculation and displays the result."""
    global calculation
    try:
        result = str(eval(calculation))  # Evaluate the mathematical expression
        calculation = result  # Store the result for further calculations
        text_result.delete(1.0, "end")  # Clear the display
        text_result.insert(1.0, result)  # Display the result
    except:
        clear_field()  # Clear the display if an error occurs
        text_result.insert(1.0, "Error")  # Show an error message