file = open("File.txt", "w")
file.write("Hello\n")
file.write("Everyone")


with open("File.txt", "r+") as file:  # this code starts beginning
    file.seek(14)
    file.write("Good Morning")


with open("File.txt", "r") as file:  # We defined file object

    content = file.read()
    print(content)
    """
    file.seek(0)  # this method set cursor to the beginning
    content2 = file.read()
    print(content2)
    """

"""
    Update something in the middle
"""

with open("File.txt", "r+") as file:
    list = file.readlines()
    list.insert(1, "Coding")
    print(list)
    file.seek(0)
    list.insert(1, "Programming")
    file.writelines(list)
