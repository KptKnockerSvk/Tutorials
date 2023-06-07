def check_game(grid, rows, columns, player_symbol):
    for row in range(0, rows):
        if grid[row] == [player_symbol] * rows:
            return True

    for column in range(0, columns):
        temp_arr = []
        for row in range(0, rows):
            temp_arr.append(grid[row][column])
        if temp_arr == [player_symbol] * rows:
            return True

    temp_arr = []
    for row in range(0, rows):
        temp_arr.append(grid[row][row])
    if temp_arr == [player_symbol] * rows:
        return True

    temp_arr = []
    for row in range(0, rows):
        temp_arr.append(grid[row][rows - row - 1])
    if temp_arr == [player_symbol] * rows:
        return True
    return False