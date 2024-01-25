#1
def size(item):
    return len(item)

list1=list(map(size,('a','sjakf','oksf','ks;lfjsalf','dl;fsajdlf  k;')))
print(list1)

#2
def add(num1,num2):
    return num1+num2

list1=list(map(add,(1,2,3),(4,5,6)))
print(list1)

#3
print(type(map(add,(1,2,3),(4,5,6))))
print(map(add,(1,2,3),(4,5,6)))

#4
for item in map(size,('ajf','kdf;',';dfk;lasjf')):
    print(item)

#5
print(list(map(lambda x:x**2,[1,2,3,4,5])))
print(list(map(lambda x,y:x+y,[1,2,3],[4,5,6])))