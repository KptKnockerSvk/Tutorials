class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hi(self):
        print(f"Hi my name is {self.name} {self.surname}")

class Manager(Employee):
    def __init__(self, name, surname, department):
        #Employee.__init__(self, name, surname) //
        super().__init__(name, surname)
        self.department = department

    def say_hi(self):
        super().say_hi()
        print(f"My department is {self.department}")

    def get_department(self):
        print(f"My department is {self.department}")

class VicePrezident(Manager):
    pass


vp = VicePrezident("Adam", "Franko", "IT")
vp.say_hi()

print(isinstance(vp, Employee))

employee = Employee("Adaffm", "Franko")
manager = Manager("Adam", "Franko", "IT")

employee.say_hi()
manager.say_hi()

print(isinstance(employee, Employee))
print(isinstance(manager, Employee))
print(isinstance(employee, Manager))

print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))


