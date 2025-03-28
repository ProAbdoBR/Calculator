def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"


def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y  # Fixed spelling


while True:
    num1 = float(input("What's your first number? "))
    num2 = float(input("What's your second number? "))  # Fixed input issue

    state = True
    while state:
        operation = input(
            "What do you want to do? (di for divide, mu for multiply, ad for add, su for subtract): ").strip().lower()

        if operation == "di":
            print("Your result is: " + str(divide(num1, num2)))  # Fixed string concatenation
            state = False
        elif operation == "mu":
            print("Your result is: " + str(multiply(num1, num2)))
            state = False
        elif operation == "ad":
            print("Your result is: " + str(add(num1, num2)))
            state = False
        elif operation == "su":
            print("Your result is: " + str(subtract(num1, num2)))
            state = False
        else:
            print("Invalid input. Please enter di, mu, ad, or su.")  # Better error message
