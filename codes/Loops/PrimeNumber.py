"""
    Question :
        Print prime numbers between two given number...
"""

num1 = int(input("Start Point : "))
num2 = int(input("End Point : "))

for i in range(num1,num2+1):
    if(i == 2)or(i == 3):
        print(i) 
    elif(i % 2 != 0) and (i % 3 != 0) and (i != 1):
        print(i)