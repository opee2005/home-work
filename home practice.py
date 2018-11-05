name = "lawal"
for i in range(len(name)):
    print(name[:i+1],end='')
    
# number 1
from math import* # this will imports all math functions
time = float(input("what is the current time: "))
hours_ahead = float(input("how many hours ahead: "))
new_time = time+hours_ahead%12
print("it will be", new_time,"o'clock in", hours_ahead, "hours  time")

# number 2
 #how many of the squares from 1 to 100 end in 4
count = 0
for i in range(1,101):
    if (i**2)%10==4:
        count=count+1
print(count)

# number 3.
# to count how many multiple of twelves in 1 to 10001
from random import randint  
count = 0
for i in range(1,10001):
    rand_num = randint(1,100)
    if rand_num%12==0:
        count+= 1
print(count)

# number 4.
x = 0
list_d = ['justin','aplle','food',3231,'another',390122]
list_e = []
for i in list_d:
    if isinstance(i, int):
        list_e.append(i)
        list_d.pop(x)
    x = x+1
    if list_d.isalpha():
       list_d = list_d[0].upper() + list_d[1:].lower()    
print(list_e)
print(list_d)

# number 5.
items = [23, 46, 80, 21, 4, 5, 1, 7, 2]
new_items = []
for i in items:
    if isinstance(i, int):
        new_items.append(i)
new_items = sorted(new_items)
print(new_items)
print(items)
    
    



            

