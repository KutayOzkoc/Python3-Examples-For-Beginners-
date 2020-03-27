"""
    Function returns while our escape method doesnt work
"""


def power(num):
    def inner(powernum):
        return num ** powernum

    return inner


two = power(2)
three = power(3)  # Number
print(two(3))
print(three(4))  # Power number


def Permission(page):
    def inner(role):
        if(role == 1):
            return ("Can access everywhere")
        else:
            return ('Cant access')
    return inner


permnum = Permission("Product")
print(permnum(1))  # Can Access Everywhere
print(permnum(2))  # Cant Access

"""
    Example for calculate fibonacci
"""


def Fibonacci(number):
    if not isinstance(number, int):
        raise TypeError("Enter Integer Number")

    if (number <= 1):
        return number
    else:
        return (Fibonacci(number-1)+Fibonacci(number-2))


number = int(input("How many term ? "))

for i in range(number):
    print(Fibonacci(i))
