"""This is a simple calculator program that performs basic arithmetic operations based
on user input with functions that return output."""

import Calculator_art

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):  
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract, 
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(Calculator_art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            calculator()

calculator()
