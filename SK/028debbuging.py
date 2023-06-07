from B028 import custom_sum

def mystery_function(x, y):
    sum = 0
    for i in range(x, y+1):
        breakpoint()
        sum = custom_sum(sum, i)
        print("A D C")
    return sum

x = 2
y = 10
breakpoint()
print(mystery_function(x, y))