#1
def func(n):
    return lambda a:a*n

double=func(2)
num=double(13)
print(num)

triple=func(3)
num=triple(5)
print(num)