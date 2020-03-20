"""
    Question :
        Create a basic mathematics calculator
"""


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1-num2


def multiplication(num1, num2):
    return num1*num2


def division(num1, num2):
    return num1/num2


def calculator(choice, num1, num2):

    switcher = {
        1: addition(num1, num2),
        2: subtraction(num1, num2),
        3: multiplication(num1, num2),
        4: division(num1, num2)
    }
    print(f"Your choice is : {choice}")
    return switcher.get(choice)


num1 = float(input("First number for calculation : "))
num2 = float(input("Second number for calculation : "))

choice = int(
    input("1-) Addition \n2-) Subtraction \n3-) Multiplication\n4-) Division\n"))

print(calculator(choice, num1, num2))
