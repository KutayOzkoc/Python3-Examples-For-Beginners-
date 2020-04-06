from datetime import datetime

# This module about date or time



result = datetime.now() # Result is datetime now 

result = result.month # result bring datetime from result then use only month.

result2 = datetime.now() # That means result2 equal datetime now

result4 = datetime.ctime(result2) # It looks better

result5 = datetime.strftime(result2,'%Y') # We can use like this too

"""
 Classical Age Problem
"""

birthday =  datetime(1999,8,6,0,0,0)

age = result2 - birthday # We can calculate our birthday


print(result)
print(result2)
print(result4)
print(result5)

print(age)
