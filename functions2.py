def isEvenElement(list1):
    list2=[]
    for num in list1:
        if (num%2==0):
            list2.append(True)
        else:
            list2.append(False)
        
    return list2


mylist=[1,2,3,4,5,6,7,8,9,10]
mylistresult=isEvenElement(mylist)
print(mylistresult)

