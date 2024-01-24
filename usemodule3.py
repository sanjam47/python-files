import module1

def myfunc1():
    print("abc")


myfunc1()

module1.myfunc()
__name__=module1

if __name__=='__main__':
    print(f'I am executing directly {__name__}')
else:
    print(f'I am executing indirectly from {__name__}')


