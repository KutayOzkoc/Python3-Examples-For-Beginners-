class Person:
    address = 'No information'

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def intro(self):
        print('Hi' + self.name)

    def calculateAge(self):
        return 2020 - self.year


p1 = Person('James', 1999)
p2 = Person('David', 1980)
p1.intro()  # we call our method from class it works for p1 object
print(f'Name = {p1.name} and Year = {p1.year}')

ageP1 = p1.calculateAge()  # We can calculate something with use class methods
ageP2 = p2.calculateAge()

print(f'{p1.name} is {ageP1} years old')
print(f'{p2.name} is {ageP2} years old')


"""
    Let's Calculate circum and area for circle
"""


class Circle:
    # class attribute
    pi = 3.14

    # constractor
    def __init__(self, radius):
        self.radius = radius

    # class Methods
    def CalculationCircum(self):
        return self.pi*self.radius*2

    def CalculationArea(self):
        return self.pi*self.radius*self.radius


radius1 = int(input('Radius for first Circle : '))
radius2 = int(input('Radius for Second Circle : '))

c1 = Circle(radius1)
c2 = Circle(radius2)

c1Circum = c1.CalculationCircum()
c2Circum = c2.CalculationCircum()

c1Area = c1.CalculationArea()
c2Area = c2.CalculationArea()

print(f'First circle area = {c1Area} and First circle circum = {c1Circum}')
print(f'Second circle area = {c2Area} and Second circle circum = {c2Circum}')
