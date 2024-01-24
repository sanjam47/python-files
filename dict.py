num={'one':1,'two':2,'three':3}
print(num)

print(num['one'])

num={'one':1,'two':2,'three':3,'four':{4:'iv'}}
print(num['four'])

num={'one':1,'two':[2,'ii','II'],'three':3}
print(num['two'][2])
print(num['two'][2].lower())
print(num)

num['two']=2
print(num)