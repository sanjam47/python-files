list1=[(1,2),(2,3),(3,4),(4,5)]


for tuples in list1:
    print(tuples)

for num1,num2 in list1:
    print(num1,num2)

dict1={'one':1,'two':2,'three':3}

#By default it prints the key values. 
for num1 in dict1:
    print(num1)

#values() will print values
for num1 in dict1.values():
    print(num1)

for key,value in dict1.items():
    print(key,value)