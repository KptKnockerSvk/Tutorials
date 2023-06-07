#Overloading
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hello(self, name=None, surname=None):
        if name and surname:
            print(f"Hello {self.name} {self.surname}")
        elif name:
            print(f"Hello {self.name}")
        else:
            print("Hello")
"""person = Person("A", "F")
person.say_hello()
person.say_hello(name=True)
person.say_hello(name=True, surname=True)"""

#overriding
class Employee(Person):
    def say_hello(self):
        print("I am employee and i will say something completely different than Person")

class Student(Person):
    def __init__(self, name, surname, studentId):
        super().__init__(name, surname)
        self.studentId = studentId


empl = Employee("A", "F")
empl.say_hello()

stud = Student("A", "F", 100)
print(stud.studentId)