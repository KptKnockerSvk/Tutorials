class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")

print(Person("Adam", "Franko"))