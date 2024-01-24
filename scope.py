name='global'

def func1():
    global name #Now changes would happen to global as we have called it.

    name='local'
    def func2():
        name='function local'
        print(f'I am {name}.')
    func2()

func1()