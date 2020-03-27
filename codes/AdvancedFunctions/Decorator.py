"""
    if we want to use one attribute or function more than one place 
    we need to create decorator function
    we can connect decorator function with others

"""


import time
import math


def my_decorator(func):
    def wrapper():
        print("Operations Before Function ")
        func()
        print("Operations After Function ")
    return wrapper


@my_decorator  # We give sayHi to decorator directly
def sayHi():
    print("Hi")


@my_decorator  # We give sayGreeting to decorator directly
def sayGreeting():
    print("Greeting")


#sayHi = my_decorator(sayHi)
#sayGreeting = my_decorator(sayGreeting)
# We defined decorator for 2 functions


sayGreeting()
sayHi()


"""
    Lets Make An Example
"""


def timecalc(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)

        finish = time.time()
        print("Function Time = " + str(finish-start))
    return inner


@timecalc
def power(a, b):
    print(math.pow(a, b))


@timecalc
def factorial(x):
    print(math.factorial(x))


power(2, 3)
factorial(4)
