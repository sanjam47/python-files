set1={1,2,3,5,56}
print(set1)

print(2 in set1)

for i in set1:
    print(i)

set1.add(6)
print(set1)

set1.update({1,3,3,5,32,3435632})
print(set1)

print(set1)
#set1.remove(8)
set1.discard(8)
print(set1.pop())

for x in set1:
    print(x)

#methods
fruits={'apple','banana','mango'}
companies={'apple','google','microsoft'}

fc=fruits.union(companies)
print(fc)

fruits.update(companies)
print(fruits)

fruits={'apple','banana','mango'}
companies={'apple','google','microsoft'}
fruits.intersection_update(companies)
print(fruits)

fruits={'apple','banana','mango'}
companies={'apple','google','microsoft'}
fc=fruits.intersection(companies)
print(fc)


fruits={'apple','banana','mango'}
companies={'apple','google','microsoft'}
fruits.symmetric_difference_update(companies)
print(fruits)

fruits={'apple','banana','mango'}
companies={'apple','google','microsoft'}
fc=fruits.symmetric_difference(companies)
print(fc)

x=fruits.copy()
print(x)