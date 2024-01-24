list1=[1,3,'abc','13',30.24]
print(list1)
print(len(list1))
print(type(list))

list2=list([1,2,3.23,'abc'])
print(list2)

print(list1)
print(list1[:])
print(list1[:4])
print(list1[1:3])
print(list1[-1])
print(list1[:-1])
print(list1[-1:])

#to check item exists.
if 1 in list1:
    print('Yes')
else:
    print('No')

print(list1)
list1[1:2]=[2,3,4]
print(list1)
print(list1)
list1.insert(4,5)
print(list1)

print(list2)

list1.append(30.25)
print(list1)

#It is use to extend the list and add any other iterable like set,tuple,list to the exisiting list.
list1.extend(list2)
set1={1,2,3,3,3,3}
print(set1)
print(list1)
list1.extend(set1)
print(list1)

#to remove any item in list
print(list1)
list1.remove(1)
print(list1)

#pop() also removes.without specified argument it removes last item.
print(list1)
list1.pop()
list1.pop(1)
print(list1)

#delete also removes the item with specified index.
del list1[1]

#deltes all items in list but list still remains.
list1.clear()
print(list1)

#loop in list
list3=list(range(10))
print(list3)

for num in list3:
    print(num)