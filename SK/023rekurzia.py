# rekurzia je funkcia ktora v sebe vola samu seba
# POZOR rekurzia musi niekedy prestat INAC nastane problem
# def simple_recursion(number):
#     print("Number is", number)
#     if number > 0:
#         simple_recursion(number - 1)
#
#
# simple_recursion(4)


# Co sa stane ked budeme printovat az po vnarani?
# DU nakreslit graf
# def simple_recursion2(number):
#     if number > 0:
#         simple_recursion2(number - 1)
#     print("Nnnumber is", number)
#
#
# simple_recursion2(5)


# # Vypocet faktorialu
# def factorial(number):
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)
#
#
# print(factorial(10))


# Fibonacci numbers
# def fibonacci(number):
#     if number == 1:
#         return 0
#     if number == 2:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)


# print(fibonacci(5))

# DU napiste kod ktory vezme string a otoci ho naopak s vyuzitim rekurzie

help_string = "jablko"
y = len(help_string) - 1
x = 0
stringg = ""

def string_rec(string, h_x, h_y, stringgg):
    h_x += 1
    stringgg += string[h_y]
    #print(stringgg)
    if h_x < h_y + h_x and h_x != 0:
        string_rec(string, h_x, h_y - 1, stringgg)
    print(stringgg)

string_rec(help_string, x, y, stringg)