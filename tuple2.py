tuple1=(1,2,3)

print(tuple)
print(type(tuple))


tuple2=(1)
print(type(tuple2))

#for one item we have to add a comma(,).
tuple3=tuple((1,))
print(type(tuple3))
print(len(tuple3))

tuple4=tuple(("apple","watermelon","banana"))
print(tuple4)
print(len(tuple4))
list1=list(tuple4)
y=list1[1]
print(y)
list1.append('cherry')
tuple4=list(list1)
print(tuple4)
list1.pop()
tuple4=tuple(list1)
print(tuple4)

(a,b,c)=tuple4
print(a,b,c)

for i in range(len(tuple4)):
    print(tuple4[i],' ')

#tuple functions 
print(tuple4)
print(tuple4.count('banana'))
print(tuple4.index('banana'))

tuple5=('banana',)
tuple4+=tuple5
print(tuple4)
print(tuple4.count('banana'))
print(tuple4.index('banana',))