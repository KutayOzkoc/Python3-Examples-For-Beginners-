"""
Question 1:
    We have a list which has numbers
        1)Find the numbers which divides by 3 without remainder
        2)Add all numbers
        3)Square all numbers in the list

Question 2:
    We have a list which has city names
    find the city name has more character than 5

Question 3:
    we have 5 product information in our list
    what is total price?
    find the products which have under 5000 price.
"""
number = [1,3,5,7,9,12,19,21]
city = ['NewYork','Ankara','London','Paris','Madrid']
products = [
    {'name':'a s1','price':'1000'},
    {'name':'a s2','price':'2000'},
    {'name':'a s3','price':'3000'},
    {'name':'a s4','price':'4000'},
    {'name':'a s5','price':'5000'}
]

#1
sum = 0
for i in number:
    sum += i
    if(i % 3 == 0):
        print(i)

print("\n")

for j in number:
    j = j*j
    print (j)

print (f"\nSum : {sum} \n")

#2
for c in city:
    if(len(c) > 5):
        print(c)


#3
pricesum = 0
for k in products:
    pricetemp = int(k['price'])
    pricesum += pricetemp

print(f"\nPrice sum : {pricesum}\n")

for k in products:
    if(int(k['price'])<5000):
        print(k['name'])
