#global scope

x = ' global x'


def Function():
    # local scope
    x = 'local x'
    print(x)  # there is local value


Function()
print(x)  # there is global value

# Example
fruit = 'apple'


def Fruits():
    fruit = 'Banana'

    def printer():
        print("I love " + fruit)

    printer()


Fruits()


# Example 2
x = 10


def convertx():
    global x  # Change Global Value In Local Scope
    print(f'X : {x} ')
    x = 100
    print(f'New X : {x}')


convertx()
print(x)
