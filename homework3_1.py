option = input("Hi! I'm your calculator, choose an option (+, -, *, /): ")

if option == "+":
    print("You've chosen addition! Please enter numbers:")
    number1 = float(input("Number one: "))
    number2 = float(input("Number two: "))
    result = number1 + number2
elif option == "-":
    print("You've chosen subtraction! Please enter numbers:")
    number1 = float(input("Number one: "))
    number2 = float(input("Number two: "))
    result = number1 - number2
elif option == "*":
    print("You've chosen multiplication! Please enter numbers:")
    number1 = float(input("Number one: "))
    number2 = float(input("Number two: "))
    result = number1 * number2
elif option == "/":
    print("You've chosen division! Please enter numbers:")
    number1 = float(input("Number one: "))
    number2 = float(input("Number two: "))
    if number2 != 0:
        result = number1 / number2
    else:
        print("You can't divide by zero!")
        result = None
else:
    print("Unknown operation!")
    result = None

if result is not None:
    print("Result: ", result)