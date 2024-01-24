def square(num):
    return num**2

list1=[1,2,3,4,5]

print(list(map(square,list1)))
print(list(filter(square,list1)))

for num in map(square,list1):
    print(num, sep=' ')

def checkEven(str=''):
    if(len(str)%2==0):
        return True
    else:
        return False
    
list2=['Micheal','Stary','John','Jacob']

print(list(map(checkEven,list2)))

print(list(filter(checkEven,list2)))