import pandas as pd

# Initialize an empty DataFrame to store history
history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

def add_to_history(operation, op1, op2, result):
    global history
    new_entry = pd.DataFrame([[operation, op1, op2, result]], 
                             columns=['Operation', 'Operand1', 'Operand2', 'Result'])
    history = pd.concat([history, new_entry], ignore_index=True)

def save_history():
    history.to_csv('calculation_history.csv', index=False)

def load_history():
    global history
    try:
        history = pd.read_csv('calculation_history.csv')
        print("History loaded successfully.")
    except FileNotFoundError:
        print("No previous history found.")

def clear_history():
    global history
    history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
    print("History cleared.")

