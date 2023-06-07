FILE_NAME = "01a.txt"

def load_data(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return lines

def process_elfs(lines):
    elfs = []
    elf = []

    for line in lines:
        if line == "\n":
            elfs += [sum(elf)]
            elf = []
            continue
        elf += [int(line)]

if __name__ == "__main__":
    lines = load_data(FILE_NAME)
    print(lines)