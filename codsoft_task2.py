# Function def
def perform_operation(num1, num2, operation):
    if operation == '1':
        #Addition
        return num1 + num2
    elif operation == '2':
        #Subtraction
        return num1 - num2
    elif operation == '3':
        #Multiplication
        return num1 * num2
    elif operation == '4':
        #Division
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '5':
        #Modules
        return num1 % num2
    else:
        return "Invalid operation"

# Main code
while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for modulo")
    print("Enter '6' to exit")

    choice = input("Enter your choice: ")

    if choice == '6':
        print("Calculator exiting. Goodbye!")
        break

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = perform_operation(num1, num2, choice)
        print("Result: ", result)
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
