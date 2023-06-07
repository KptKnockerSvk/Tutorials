FILE_NAME = "03a"


def read_file(file_name):
    result = []
    with open(file_name, "r") as f:
        for line in f:
            result.append(line.strip())
        xx = len(result)
        return result, xx

def process_bags(bags):
    result = 0
    for bag in bags:
        result += encode_char(process_bag(bag))
    return result

def process_bag(bag):
    middle = int(len(bag)/2)
    for e in bag[:middle]:
        if e in bag[middle:]:
            return e

def encode_char(charc):
    if ord(charc) >= ord("a"):
        return ord(charc) - ord("a") + 1
    else:
        return ord(charc) - ord("A") + 27

def process_bags2(bags, number_in_group):
    i = 0
    result = 0
    while i < len(bags):
        e = process_group(bags[i:i+number_in_group], number_in_group)
        result += encode_char(e)
        i += number_in_group
    return result

def process_group(group, xx):
    for e in group[xx - 3]:
        if e in group[xx - 2] and e in group[xx-1]:
            return e



if __name__ == "__main__":
    bags, xx = (read_file(FILE_NAME))
    #print(process_bags(bags))
    print(process_bags2(bags, xx))


#Nefunkčný multiple group -- number_in_group