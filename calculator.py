import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error("Attempt to divide by zero")
        return "Error: Division by zero"

def repl():
    print("Welcome to the Python Calculator. Type 'exit' to quit.")
    while True:
        command = input("Enter operation and two numbers (e.g., 'add 2 3'): ").strip().split()
        if command[0].lower() == 'exit':
            print("Exiting... Goodbye!")
            break
        try:
            operation, num1, num2 = command[0], float(command[1]), float(command[2])
            if operation == 'add':
                print(f"Result: {add(num1, num2)}")
            elif operation == 'subtract':
                print(f"Result: {subtract(num1, num2)}")
            elif operation == 'multiply':
                print(f"Result: {multiply(num1, num2)}")
            elif operation == 'divide':
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Unknown operation. Please try again.")
        except (ValueError, IndexError):
            logging.error("Invalid input. Correct format: operation num1 num2")
            print("Error: Invalid input. Please try again.")

if __name__ == "__main__":
    repl()

