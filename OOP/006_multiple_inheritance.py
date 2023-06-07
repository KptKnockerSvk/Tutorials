"""class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hi(self):
        print("Hi")

class Employee:
    def say_hello(self):
        print("Hello")

class Manager(Person, Employee):
    pass

manager = Manager("Michal", "Hucko")
manager.say_hello()
manager.say_hi()"""

class A:
    name = "A"

class B(A):
    name = "B"
    def __init__(self, b):
        self.b = b

class C(A):
    name = "C"
    def __init__(self, c):
        self.c = c
class D(C,B):
    name = "D"
    def get_super(self):
        print(super().name)

d = D ("text")
d.get_super()
print(d.c)

print(B.mro())