"""

    Question 1:
        We have a list about numbers and print them 
        with using while loop
    Question 2:
        Enter 2 number and print all numbers between
        them
    Question 3:
        print numbers between 1-100 with decreasing rule
    Question 4:
        Take 5 number from user and sort them then print
        all of this number
    Question 5:
        Enter some products in product list
        with name and price
        take number of products 
        and print them
    
"""

numbers = [1,3,5,7,9,12,19,21]


#1
k = 0
while (k < len(numbers)):
    print(numbers[k])
    k += 1

print("\n")

#2
x = int(input("First Number : "))
y = int(input("Second Number : "))

while (x <= y):
    print (x)
    x += 1

print("\n")

#3
ctr = 100
while (ctr >= 1):
    print(ctr)
    ctr -= 1

print("\n")

#4
numbers2 = []
i = 0
while (i<5):
    num = int(input("Enter Number"))
    numbers2.append(num)
    i += 1


print (sorted(numbers2))

print("\n")

#5
products = []

Productnum = int(input("How Many Product will you enter ?"))

counter = 0
while (counter < Productnum):
    name = input('Name : ')
    price = int(input('Price : '))
    products.append({
        'Name':name,
        'Price':price
    })
    counter += 1

print(products)