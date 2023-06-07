class Person:
    pi = 3,1415
    def __init__(self, name):
        self.name = name

adam = Person("Adam")
lenka = Person("Lenka")
print(adam.name)
print(lenka.name)
print(Person.pi)
print(lenka.pi)

#adam.pi = 4  //
Person.pi = 4

print(Person.pi)
print(lenka.pi)
print(adam.pi)

"""class Employee:
    base_salary = 500
    def print_base_salary(self):
        print(Employee.base_salary)
        self.base_salary = 1000
        print(Employee.base_salary)
        print(self.base_salary)
emp = Employee()
emp.print_base_salary()"""