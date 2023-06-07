class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.name + " " + self.surname

    #def __add__(self, other):
     #   return self.age + other.age
    def __add__(self, other):
        return Marriage(self, other)

    def __eq__(self, other):
        return self.age == other.age

    def __neg__(self):
        temp = Person(self.name, self.surname, self.age)
        temp.age = -temp.age
        return temp

class Marriage:
    def __init__(self, husband, wife):
        self.husband = husband
        self.wife = wife

    def __str__(self):
        return self.husband.name + " " + self.wife.name + " " + self.husband.surname

adam = Person("Adam", "Franko", 23)
lenka = Person("Lenka", "Frankoba", 22)
print(adam + lenka)
print(adam)

print(adam.age)
print(-adam.age)