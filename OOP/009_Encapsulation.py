class Curve:
    slope = 3
    __center = 10   #Private

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __print_slope(self):
        print(Curve.slope)

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value
    def set_y(self, value):
        self.__y = value

    def print_coordinates(self):
        print(f"x: {self.__x} y: {self.__y}")

line = Curve(3, 4)
print(Curve.slope)
line.print_coordinates()
print(Curve._Curve__center)
print(line._Curve__x)
line._Curve__print_slope()

print(line.__dict__)
print(Curve.__dict__)

class SpecialLine(Curve):
    pass

sl = SpecialLine(2, 2)
print(sl._Curve__center)
