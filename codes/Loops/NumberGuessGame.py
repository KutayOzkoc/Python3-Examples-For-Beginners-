"""
        We will create a basic game for check our daily 
    chance point
        We will use specific module for get random number
        Numbers are between 1-10 and user give a number then
    -if user cant find the random number in 5 attempts means 0 point
    -else if user can find in one shot 10 point 
    -else if can find 2 shot 8 point
    -else if can find 3 shit 6 point
    -then it goes to 0 point...  
        random.radint(start point,end point) specific function for generate random values
"""
import random

number = random.randint(1,10)
print (number)

i = 1
for i in range(10):
    unumber = int(input('Enter a Number for check your daily chance :) \n'))
    if(unumber == number):
        i += 1
        print(f"You can find in {i} attemps")
        break

if(i == 5):
    print("Your chance point is 2")
elif (i == 4):
    print("Your chance point is 4")
elif (i == 3):
    print("Your chance point is 6")
elif (i == 2):
    print("Your chance point is 8")
elif (i == 1):
    print("Your chance point is 10")
else:
    print("Your chance point is zero :(")    