list1=[1,2,3,4,5,6]
#prints all the numbers in list
for num in list1:
    print(num)

#prints all the even numbers in list
for num in list1:
    if(num%2==0):
        print(num)

sum=0
#prints the sum of all numbers in list
for num in list1:
    sum+=num
print(sum)


friends=['Rahul','Jane','Riya','Mohit','Daksh']

#prints all the  name of friends of length 4
for names in friends:
    if(len(names)==4):
        print(names)


