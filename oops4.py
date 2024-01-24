class Animal:
    def __init__(self):
        print('Animal created')
    
    def whoAmI(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating...')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created.')
    
    def whoAmI(self):
        print('I am a dog')

A1=Animal()
D1=Dog()

D1.__init__()
D1.whoAmI()
#Inherited method.
D1.eat()

