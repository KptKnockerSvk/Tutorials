class Car:
    def __init__(self, wheels, number_of_doors):
        self.__wheels = wheels
        self.__number_of_doors = number_of_doors
    @staticmethod
    def vrm_vrm():
        print("Vrm vrm")

    def get_car_doors(self):
        return self.__number_of_doors

class Mercedez(Car):
    pass

class Bmw(Car):
    def __init__(self, wheels, number_of_doors, color):
        super().__init__(wheels, number_of_doors)
        self.color = color

class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Manager(Employee):
    def __init__(self, name, surname, car):
        super().__init__(name, surname)
        self.car = car
    def get_car_doors(self):
        return self.car.get_car_doors()

manager = Manager("Adam", "Franko", Bmw(4, 3, "blue"))
print(manager)
print(manager.get_car_doors())