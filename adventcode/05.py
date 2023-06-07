FILE_NAME = "05a"

def move_crate(stacks, moves):
    for move in moves:
        moving = stacks[move[1]][:move[0]]
        for c in moving:
            stacks[move[2]] = [c] + stacks[move[2]]
        stacks[move[1]] = stacks[move[1]][move[0]:]
    return stacks


def process_file(file_name):
    stacks  = {}
    moves = []
    with open(file_name, "r") as f:
        for line in f:
            if line == "\n" or line[1] == "1":
                continue
            if not line.startswith("m"):
                for stack, crate in enumerate(range(1, len(line), 4)):   # 4 = po koľkom kroku, 1 - 5
                    if line[crate] != " ":
                        current_stack = stacks.get(stack + 1, [])
                        stacks[stack + 1] = current_stack + [line[crate]]
            if line.startswith("m"):
                parts = line.split()
                moves.append([int(parts[1]), int(parts[3]), int(parts[5])])
    return stacks, moves


if __name__ == "__main__":
    stacks, moves = process_file(FILE_NAME)
    #print(stacks ,"\n",  moves)
    stacks = move_crate(stacks, moves)
    #print(stacks)
    result = ""
    for i in range(1, len(stacks.keys()) + 1):
        result += stacks[i][0]
    #print(result)