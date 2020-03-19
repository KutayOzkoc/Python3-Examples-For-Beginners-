"""
---Without Using Loops---

Question 1: 
    Enter a number and look its between 1-100 or not?

Question 2:
    Enter a number and look its positive or negative?

Question 3:
    Check Mail and password question

Question 4:
    Compare the values of three numbers entered

Question 5:
    Take 2 midterm and 1 final points for gpa calculation
    and if average > 50 write pass the exam

"""
#1
number = float(input("Enter a number !!!"))
print(f"{number}")

if(number > 1) and (number < 100):
    print("Good number for your condition...")
else:
    print("This number is not in your condition")


#2
if(number > 0):
    print("Number is positive")
else:
    print("Number is negative")

#3
email = "abc@abc.com"
password = 1234

Email = input("Enter your Email\n")
Password = int(input("Enter your password"))

if (email == Email) and (password == Password):
    print("Login successful")
else:
    print("Login failed")

#4
midterm1 = float(input("Midterm 1: "))
midterm2 = float(input("Midterm 2: "))
Final = float(input("Final 3: "))

average = ((midterm1+midterm2)/2)*0.6 + (Final*0.4)

print(f"Your average : {average}")

if (average > 50):
    print("You passed the course ")
else:
    print("Failed")





