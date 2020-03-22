"""
    Whats Modules ? 
    We divide our applications and we call modules to each piece
    Modules have connections between them
    We always have main module for run applications

    We have 2 tyoe modules
     1-> modules we have prepared
     2-> ready modules
      a-> Standart
      b-> Third party modules
            We can install them with using pip install < package_name >
"""

"""
    Let we use math module for example
"""


"""
value = dir(math) # We can see all function in math module with this
value = help(math)  # We can see how can we use this module
value = help(math.factorial)  # Just Factorial
"""


import mod
import random
import math as calculation # Also we can use like that
import math  # import module here
from math import *  # import everything
num = calculation.factorial(5)
num2 = factorial(3)
print(num)
print(num2)


"""
    Let we use random module for example
"""

cities = ['Ankara', 'California', 'Berlin']

result = cities[random.randint(0, len(cities)-1)]

list = range(100)
result2 = random.sample(list, 3)
print(result)
print(result2)


"""
    Let's create a module
"""
resultmod = mod.person['name']
p = mod.Person()
p.speak()
print(resultmod)
