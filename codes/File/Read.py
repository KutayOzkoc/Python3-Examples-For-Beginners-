"""
    Create file for read 
"""
file = open("newFile.txt", "w")
file.write("Hello Everyone \n")
file.write("Lets continue tutorial")


# We need to check the file exist or not
try:
    file = open("newFile.txt", "r")
except FileNotFoundError:
    print("!!! File Does Not Exist !!!")


# We can read everything from file
"""
for i in file:
    print(i)
"""
# We can read without using loop
"""
content = file.read()
print(content)
"""
# Read just five character
"""
content = file.read(5)
print(content)
"""
# We can read line by line
"""
print(file.readline())
"""
# We can read lines and add them into a list
"""
list = file.readlines()
print(list)
"""


file.close()
