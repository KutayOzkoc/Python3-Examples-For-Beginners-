"""
    Create a program for basic students information system.
"""


def Display():
    with open("Grades.txt", "r", encoding="UTF-8") as file:
        for row in file:
            print(Average(row))


def Enter():
    name = input('Name : ')
    lname = input('lname : ')
    grade1 = (input('First Grade : '))
    grade2 = (input('Second Grade : '))
    Final = (input('Final Grade : '))
    with open("Grades.txt", "a", encoding="UTF-8")as file:
        file.write(name + " " + lname+":" + grade1+","+grade2+","+Final+'\n')


def Save():
    with open('Grades.txt', "r", encoding="utf-8")as file:
        list = []
        for i in file:
            list.append(Average(i))

        with open("Results.txt", "w") as file2:
            for i in list:
                file2.write(i)


def Average(row):
    row = row[:-1]
    list = row.split(':')
    studentinfo = list[0]
    grades = list[1].split(',')

    grade1 = float(grades[0])
    grade2 = float(grades[1])
    final = float(grades[2])

    average = (grade1 + grade2 + final)/3
    average = str(average)
    return 'Student name : ' + list[0] + ' Student Average : ' + average + "\n"


while True:
    operation = int(input(
        '1- Display Grades \n2- Enter Grades\n3- Save these Grades\n4- exit\n'))
    if (operation == 4):
        break
    elif (operation == 1):
        Display()
    elif(operation == 2):
        Enter()
    else:
        Save()
