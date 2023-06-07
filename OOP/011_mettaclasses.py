class Person:
    pass


person = Person()
print(type(4))
print(type(person))
print(type(Person))
print(type(type))

#Creating of type
# 1.name of class 2.tupple of parental class (if none, object!) 3. menný priestor
def multiline_function(self):
    print("Line1")
    print("Line2")

A = type("A", (), {"x": 10, "scitaj": lambda self,x,y: x + y, "multiline": multiline_function})
a = A()
#same as
#class A:
#   pass

print(a.scitaj(10,11))
a.multiline()

class MetaAdam(type):
    def __init__(cls, name, bases, dict):
        print("Call") #Dôkaz volania konštruktoru
        cls.Pi = 3.14

class Circle(metaclass=MetaAdam):
    pass

circle = Circle()

print(circle.Pi)
