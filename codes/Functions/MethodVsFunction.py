# Method

list = [1, 2, 3]

# Append is a method
list.append(5)

# Lots of methods defined before for developers
print(list)


# Function
# we cant define them in classes, we can use them directly their features


def sayHello():
    print("hello")


# Define our function with def

sayHello()

# Call our function
# We can call this function more than one time

sayHello()

# we can give parameters from outside the function
# we can define a default parameter for our function


def sayHello2(user='User'):
    print("User name is : " + user)


user = "User1"
sayHello2(user)
sayHello2()


# We can define function for return values

name = "Name"


def message(name="name"):
    return 'hello' + name


msg = message('names')
print(msg)
