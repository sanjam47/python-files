#1
def isEven(num):
    return num%2==0

list1=list(filter(isEven,(1,2,3,4,5)))
print(list1)

#2
print(list(filter(lambda x:x<18,[1,5,66,22,2])))