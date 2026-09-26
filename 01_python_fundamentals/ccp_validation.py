# Prompting for a temperature input (e.g., pasteurization monitor)
raw_input = input("Enter the pasteurization temperature (Celsius): ")

try:
    # Try converting the text input into a decimal number
    temperature = float(raw_input)
    print("Verification Successful. Temperature recorded:", temperature)
    
except ValueError:
    # If the user typed letters like "abc" instead of a number, Python executes this backup plan instead of crashing
    print("[ERROR]: Non-numeric data entered. Corrective action required: Please log a valid number.")

print("Data processing cycle complete. System remains operational.")