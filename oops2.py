class Dog:

    #This is the class level attribute/variable.We donot need to use self as it is already declared at class level.
    species='mammal'

    def __init__(self,breed,name,spots):
        #breed=string
        self.breed=breed
        #name=string
        self.name=name
        #spots=boolean
        self.spots=spots

    #methods/attributes
    def displayDog(self):
        if(self.spots):
            return f'Dog is of {self.breed} breed,its name is {self.name} and has no spots.'
        else:
            return f'Dog is of {self.breed} breed,its name is {self.name} and has spots.'
    
    def bark(self,count):
        while count!=0:
            print('I am barking')
            count-=1

dog1=Dog('Golden Retreiver','Tommy',True)
dog2=Dog('Labrador','Simba',False)

dog1.bark(5)

