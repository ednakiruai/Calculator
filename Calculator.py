def clear_field():
    """Clears the calculation field and resets the stored calculation."""
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the display