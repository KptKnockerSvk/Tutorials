# Dajme tomu ze mame ulohu kazde parne cislo v intervale od 0 po 20 vynasob desiatimi
# Ako by sme to vyriesili ?
numbers = range(1, 21)
result = []
for i in numbers:
    if i % 2 == 0:
        result.append(i*10)
print(result)


# Lsit comprehension
# if and else part are optional
# [<return_value> for <variable_name> in <list> if <condition>]
results = [number*10 for number in numbers if number % 2 == 0]
print(results)


# Kazde parne cisla vynasob 10 a kazde neparne cislo vynasob 30
# V list comprehensions nie je else ale vieme sa vynajst
results = [number*10 if number % 2 == 0 else number*30 for number in numbers]
print(results)


# Majme retazec na vstupe a na vystupe chceme pole cisel ktore nesie informaciu o pocte pismen pre kazde slovo v retazci
string = "Informatika s misom je cool"
# pomocou .split() funkcie viem rozdelit retazec na pole slov
print(string.split())
print([len(word) for word in string.split()])

# Triky na koniec
arr = ["this", "is", "string"]
print(" ".join(arr))


# Domaca uloha
# Napis funkciu list_of_lists ktora dostane na vstupe cez parameter pole celych cisel vacsich ako 0 napr. [0,2,3,2]
# Nasledne vrati pole cisel ktore bude obsahovat pre kazde cislo pole s cislami od 0 po to dane cislo

# pre vstup [0,2,3,2]
# vrati [[0], [0,1,2], [0,1,2,3], [0,1,2]]
# Musti to byť funkcia !!

list = [0, 2, 3, 2,5,10]
y = len(list)

def list_of_lists(h_list, y):
    d_list = []
    for yy in h_list:
        n_list = []
        z = 0
        while True:
            n_list.append(z)
            if z + 1 <= yy and yy != 0:
                z += 1
            else:
                break
        d_list.append(n_list)
    print(d_list)



list_of_lists(list, y)
