"""
    Question 1:
        Define a function that writes a given word as many times as desired 
    Question 2:
        Define a function that converts unlimited parameters sent to it to the list
    Question 3:
        Define a function that finds all prime numbers between 2 sent numbers
    Question 4:
        Define a function that returns the full divisors of the number sent to it in a list

"""

# 1


def printer(word, piece):
    print(word*piece)


word = input("Enter your word for your function : ")
piece = int(input("How many times print that word ? "))

printer(word, piece)


# 2

def convertlist(*params):  # *params means all parameters
    list = []

    for i in params:
        list.append(i)

    return list


result = convertlist(1, 2, 3, 4, 5, 'Hi', 12.5)
print(result)

# 3


def primefinder(num1, num2):
    for ctr in range(num1, num2 + 1):
        if(ctr > 1):
            for j in range(2, ctr):
                if(ctr % j == 0):
                    break
            else:
                print(ctr)


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

primefinder(num1, num2)

# 4


def fulldivisors(num):
    fulldivisor = []

    for i in range(2, num):
        if(num % i == 0):
            fulldivisor.append(i)
    return fulldivisor


num = int(input("Number for full divisors : "))

print(fulldivisors(num))
