#Use Python’s logging module to log info and error messages in a script.
import logging

# Configure logging to print to console
logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(levelname)s: %(message)s')  # Log format

# Function to divide two numbers
def divide_numbers(a, b):
    logging.info(f"Dividing {a} by {b}.")  # Log an info message
    try:
        result = a / b
        logging.info(f"Result: {result}")  # Log the result
        return result
    except ZeroDivisionError:
        logging.error("Error: Division by zero attempted.")  # Log an error message
        return None

if __name__ == "__main__":
    divide_numbers(10, 2)  # This should log info messages
    divide_numbers(10, 0)  # This should log an error message