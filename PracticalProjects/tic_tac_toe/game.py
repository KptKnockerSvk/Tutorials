from piskvorky import print_grid, create_grid
from input_handler import get_input
from game_handler import check_game

rows = 3
columns = 3
empty_sign = "_"
player_dict = {
    0: "X",
    1: "O"
}

grid = create_grid(rows, columns)
empty_places = rows*columns

move_counter = 0
game_ended = False

for round_id in range(1, 6):
    print("Round no is", round_id)
    for player in range(0, 2):
        while True:
            print("Player ", player, " turn")
            print_grid(grid, rows, columns)
            x = str(input("Enter rowY "))
            y = str(input("Enter colX "))
            if x in "012" and y in "012":
                print("Good nums and empty position ")
                x = int(x)
                y = int(y)
            else:
                print("Not good nums ")
                continue
            if grid[x][y] != empty_sign:
                print("Oooooooooopsie")
                continue
            else:
                break

        grid[x][y] = player_dict[player]
        if check_game(grid, rows, columns, player_dict[player]):
            print("Player ", player, " has won")
            game_ended = True
            print_grid(grid, rows, columns)
            break
        move_counter += 1

        if move_counter == empty_places:
            print("Draw")
            print_grid(grid, rows, columns)
            break
    if move_counter == empty_places:
        break
    if game_ended:
        print("CG, GG")
        break

