""" Základne datové tipy
str
int, float
bool
list
tuple
dict
set

# Classes ---> Custom type
WizardPlayer

# Special data types --> Extra navyše
Modules

None ---> nič

age = None

########################################################
# Math funx
print(round(5.3))   == 5
abs(-5)     == 5, absolútna hodnota

import math
print(math.sqrt(4))  == 2

########################################################
# Binárne čísla
print(bin(5))  == 0b101
bin(10) == 0b1010
print(int("0b101", 2))  ---> prevedie z bin naspak

########################################################
# Premenné
 1. Bežné
 2. Konštanty
    PI = 3.14
 3. Multi
    a, b, c = 1, 2 ,3
    x, y = y, x   --> funguje bez 3.tej premennej

########################################################
# Expresion a statement
x = 5  # St - proste tvrdenie
x / 2  # Ex - vracia novú hodnotu
y = x / 2 # Statement

########################################################
# Stringy

name[0:4:1]
    start : end : step
    [1:]     [:6] - do 6
    [::1] po kroku 1
    [-1]

########################################################
# List unpacking
list = [ "1
    "2
    "3
    "4        ]

a, *rest, g = list
print(a)  == 1
print(rest) == [2,3]
print(g) == 4
rest vytvorí list v strede

########################################################
# Tuple
first_tuple = ("z", 1, 2, 3, 4, 5)
first_tuple[0] = "a" -->nepfunguje
print(3 in first_tuple)  --> vráti True

skvelé využitie s dics
colors = {
    "red": (255,0,0),            //  (1, 2): (255,0,0) oboje môžu byť tuple
    "green": (0,255,0),
    "blue": (0,0,255)
    }

########################################################
# Set - dat.typ
f_set = {1, 2, 2, 2, 3, 8, 5, 5, 5}
print(f_set)  ---> Vypíše bez duplikácie, 1,2,3,5,8

"""
