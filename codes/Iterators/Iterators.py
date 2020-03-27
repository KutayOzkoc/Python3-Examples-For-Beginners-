"""
    Iterator usage in python
"""

list = [1, 2, 3, 4]
for i in list:
    # list is iterable object
    # i is iterator for us
    print(i)

"""
    Lets create a own iterator
"""
iterator = iter(list)
print(next(iterator))  # Firs element in our list


# We need to write excaption
# Loops work logic
while True:
    try:
        element = next(iterator)
        print(element)
    except:
        print("Out of iterator range !!!")
        break


"""
    Example
"""


class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):  # This makes it iterable
        return self

    def __next__(self):
        if(self.start <= self.stop):
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


list = MyNumbers(10, 20)

myiter = iter(list)
print(next(myiter))

for x in list:
    print(x)
