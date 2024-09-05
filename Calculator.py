def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
    return f"The result is: {result}"
print(calculator())
