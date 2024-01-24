list1=range(1,11)
for num in list1:
    print(num,end='')

print()

list2=range(1,11,2)
for num in list2:
    print(num,end='')

print()

list2=('abc','def','ghi','jkl','mno')
for index,str in enumerate(list2):
    print(index,str)

combine=zip(list1,list2)
for element1,element2 in combine:
    print(element1,element2)

print(1 in [1,2,3])
print('mykey' in {'mykey':1})