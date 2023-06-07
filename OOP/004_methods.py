from datetime import date
class Employee:
    base_salary = 400
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def got_base_salary(cls):
        print(f"Base salary is {cls.base_salary}")

Employee.got_base_salary()





class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def based_on_year(cls, name, year):
        return cls(name, date.today().year - year)

student = Student1.based_on_year("Adam", 2000)
print(student.age)






class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def sum_numbers(num1, num2):
        return num1 + num2

print(Student.sum_numbers(1, 2))
student = Student("Michal", "Hucko")
print(student.sum_numbers(1,2))