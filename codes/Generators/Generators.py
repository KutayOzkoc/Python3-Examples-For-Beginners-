"""
    Generators Create an iterartors which does not have 
    location in memory
"""


def cube():  # This is not generator
    result = []
    for i in range(5):
        result.append(i**3)
    return result


def square():
    for i in range(5):
        yield i**2  # Generate use and delete


for i in square():
    print(i)

print(cube())
Generator = square()
iterator = iter(Generator)
generator2 = (i**4 for i in range(5))
print(generator2)


print(next(iterator))
