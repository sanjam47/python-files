list1=[{'a' : 5 , 'b': 7}, {'a' : 8 , 'b': 7} , {'a' : 10 , 'b': 7}, {'a' : 1 , 'b': 7}]
# list2=list()


# for dict1 in list1:
#     for key,values in dict1.items():
#         list2=list2.append(values)
#         list2.sort()

temp_list = list()
for x in list1:
    if  len(temp_list):
        if x['a'] >max([a['a']  for a in  temp_list]):
         temp_list.insert(-1, x)
        else:
           temp_list.insert(0,x)
    else:
        temp_list.append(x)

 list1.sort(key = lambda x : x['a'], reverse = True)
        
print(f"temp_list---{temp_list}")


kk = (100, 200, 300)
mm = [kk, 1 , 2 ,3]
mm[0][1] = 'kk'
print(mm)

list(
    map (
        lambda x: x %2,
        range(1, 10)
    )
)
x  ---> 1 % 2 = 1
x---> 2 %2 = 0
x----> 3%2 = 1
[1,0, 1, 0 ,1 0, 1]


list(
    filter (
        lambda x: x %2,
        range(1, 10)
    )
)

list1=[{'a' : 5 , 'b': 7}, {'a' : 8 , 'b': 7} , {'a' : 10 , 'b': 7}, {'a' : 1 , 'b': 7}]


[{'a' : 1 , 'b': 7}, {'a' : 5 , 'b': 7}, {'a' : 8 , 'b': 7} , {'a' : 10 , 'b': 7}]

for dict1 in list:
    for  in i
        
   