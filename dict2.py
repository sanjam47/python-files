dict1={'one':1,'two':2,'three':3}
dict2=dict(one=1,two=2,three=3)

#prints the dictionary
print(dict1)
print(dict2)

#gives all the keys in dictionary. 
print(dict1.keys())
#type is of class dict_keys.
print(type(dict1.keys()))

#prints all the values in dictionary.
print(dict1.values())
#type is of class dict_values.
print(type(dict1.values()))

#prints all teh items in dictionary.
print(dict1.items())
#type is of class dict items.
print(type(dict1.items()))



#check only key pairs.we can use values() function for checking.
if 'one' in dict1:
    print('yes')
else:
    print ('no')

#update the dictionary
dict1.update(one='one')
print(dict1)
dict1.update({'one':1})
print(dict1)
dict1['one']='one'
dict1['one']=1
print(dict1)

#add items in dictionary using udpate()
dict1.update(four=4)
print(dict1)

#remove items.We can use pop() for particular key,popitem() for deleting last key:value pair
# Also usin del with specified key
#clear() empties the dictionary.

dict1.pop('one')
print(dict1)
dict1.popitem()
print(dict1)
del dict1['three']
print(dict1)
dict1.clear()
print(dict1)


#loop in dictionary.
dict1={'one':1,'two':2,'three':3}
for key in dict1:
    print(key,dict1[key])

for key,values in dict1.items():
    print(key,values)

#copy dictionaries

dict2=dict1.copy()
print(dict2)

dict2=dict(dict1)
print(dict2)

#nested dictionary
dict3=dict(one=dict(i=1),two=dict(ii=2),three=dict(iii=3))
print(type(dict3))
print(dict3)
print(dict3['one']['i'])

dict4={1:1,2:2}
print(type(dict4))
print(dict4)


#fromkeys()-
a={1,2,3}
b={'one','two','three'}
c=dict.fromkeys(a)
print(c)
c=dict.fromkeys(a,b)
print(c)

#get()- returns the value of key. We can give value with key which can be returned it value is not present.Default is null.
print(dict1.get('one','not present'))
print(dict1.get('five','not present'))

#setdefualt()- it also return the value of key.But if key is not present.It inserts it in dictionary with valeu.
print(dict1.setdefault('one','hii'))
print(dict1.setdefault('four','hii'))
print(dict1)


dict4=dict({1:2,2:3})
print(dict4)