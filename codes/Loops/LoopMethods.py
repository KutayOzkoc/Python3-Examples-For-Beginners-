"""
range():
    First start point 
    Second end point
    Third one is rule for counting

enumerate():
    Take string index and letter same loop

zip():
    Combine two list in one list

"""
for i in range(10,20,2):
    print(i)

Greetings = 'Hi everyone'

for index,letter in enumerate(Greetings):
    print(f"Index num : {index} letter : {letter}")


list1 = [1,2,3,4,5]
list2 = ['NewYork','Ankara','London','Paris','Tokyo']

list3 = list(zip(list1,list2))
print(list3)