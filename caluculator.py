def calculator():
    print("Welcome to the calculator program!")
    print("Please enter two numbers and the operation you would like to perform.")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
        return
    
    # Print the result
    print(f"{num1} {op} {num2} = {result}")

# Call the calculator function
calculator()
