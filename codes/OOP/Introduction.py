# Class
class Person:
    pass  # it means it hold a area in memory
    # we can define
    # - Class attributes
    address = 'No information'  # its for every objects

    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
        # init always runs
        print('Init method worked')
        # + methods


p1 = Person('John', 1999)
# Object , instance
# we define object for person class
# we can define more than one object in one class type
p2 = Person('Mark', 1995)
# init method works for each object


# we can access object attributes

print(f'Name = {p1.name} and Year = {p1.year} and {p1.address}')
print(f'Name = {p2.name} and Year = {p2.year}')

# Update Objects
p1.name = 'David'
print(f'Name = {p1.name} and Year = {p1.year} and {p1.address}')
# p1's name changed


# We also can define object attributes
print(p1)  # if we run this code
# <__main__.'Person' > This output says this object's type is Person Class
