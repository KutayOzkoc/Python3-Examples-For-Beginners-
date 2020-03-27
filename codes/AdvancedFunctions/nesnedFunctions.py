"""
  We will examine the nested functions  
"""


def greeting(name):
    print('Hello', name)


print(greeting('John'))

sayhello = greeting  # We make sayhello function same as greeting

print(sayhello('David'))

# Encapsulation technique
# Outer define new workscope for make its functions


def outer(n1):
    print('outer')  # Just outer function works

    def inner_increment(n1):
        print('Inner')
        return (n1 + 1)
    n2 = inner_increment(n1)  # Both of them works
    print(n1, n2)


# We cant run inner_increment out of the outer scope
outer(10)


"""
    Example for calculate function
"""


def factorial(num):
    if not isinstance(num, int):
        raise TypeError('Number must be integer')  # We can check type in there

    def inner_Fact(num):
        if(num <= 1):
            return 1
        # There we use rekursive function we will look them
        return num*inner_Fact(num-1)

    return inner_Fact(num)


print(factorial(5))
