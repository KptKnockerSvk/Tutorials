#TICTACTOE
#úvod nápisu v x
#kto je na rade
#výpis plochy listin list, _ na prázdne, x/O na zárezy
#chyby mimo poľa, znaku
#výsledok vypísať, kto vyhral, remíza, moduly

def print_grid(grid, rows, columns):
    print("  ", end = "")
    for column in range(0, columns):
        print(column, end = " ")
    print()

    for row in range (0, rows):
        print(row, end = " ")
        for column in range (0, columns):
            print(grid[row][column], end = " ")
        print()

def create_grid(rows, columns, empty_sign = "_"):
    grid = []
    for row in range (0, rows):
        temp_row = []
        for column in range (0, columns):
            temp_row.append(empty_sign)
        grid.append(temp_row)
    return grid







