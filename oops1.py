class First():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a+self.b
    
f1=First(20,30)

print(f1.a)
print(f1.b)
print(f1.add())
