"""
    The most important thing for OOP
        person -> name , age ,eat() ,run()
            student -> name ,age ,eat() ,run()

        student(Person) That means student is a person and 
        student has persons attributes and methods

        animal -> dog(animal), cat(animal)     
"""


class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print('Person Created')

    def who_am_i(self):
        print('Person')


class Student(Person):  # Person is ancestor class
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('Student Created')  # This beat Person's constructor

    # Override Student use this method for who am i
    def who_am_i(self):
        print('Student')


class Teacher(Person):
    def __init__(self, fname, lname):
        # we dont need self parameter because we use super keyword
        super().__init__(fname, lname)

    def who_am_i(self):
        print(f'I am {self.fname}')


p1 = Person('Martin', 'Matt')
s2 = Student('Josef', 'Arnold')  # Student can use Person constructor
t1 = Teacher('Ashe', 'Mark')

print(f'{p1.fname} and {p1.lname}')
print(f'{s2.fname} and {s2.lname}')

p1.who_am_i()
s2.who_am_i()
t1.who_am_i()
