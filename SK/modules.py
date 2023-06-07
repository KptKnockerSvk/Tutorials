# V pythone vieme importovat existujuci kod z ineho python suboru pomocou syntaxe
from module_folder.mathematics import addition # importing specific names from module

number1 = 2
number2 = 2
result = addition(number1, number2)

# ked importujeme ten isty nazov z dvoch rozlicnych modulov vzdy sa pouzije ten neskorsi

# Video https://youtu.be/ea6R0ZygfLM
# importovat vieme aj z priecinku alebo podpriecinku

# __init__.py sa niekedy v minulosti v starsich verziac pouzival na oznacenie priecinku ktory obsahoval python moduly

# python ponuka niekolko build in kniznic ktore vieme importovat, kniznica je subor takych python modulov
# napriklad math module
# tieto funkcie nevidime ale su nainstalovane vo vasom pc hned ako ste nainstalovali python
import math

# O tomto viac v dalsej lekcii

print(math.factorial(10)) # vrati faktorial cisla 10 