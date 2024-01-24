class Car:
    def __init__(self, name, model, car_type, length):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.length = length

    def __str__(self):
        return f'Car name is {self.name}, its model is {self.model} and type is {self.car_type}.'

    def __len__(self):
        return int(self.length)
    
    def __del__(self):
        return 'Object of car has been deleted'

C1 = Car('Ford', 'Mustang', 'Sedan', 15)

print(C1)
print(len(C1))

del C1

