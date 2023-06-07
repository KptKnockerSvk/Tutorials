FILE_NAME = "02a"
elementMapping ={
    "X": "A",
    "Y": "B",
    "Z": "C"
}

element_score = {
    "A": 1,
    "B": 2,
    "C": 3
}

enementsWin = {
    "A": "B",
    "B": "C",
    "C": "A"
}

elementsLoose = {
    "A": "C",
    "B": "A",
    "C": "B"
}

wins = ["AB", "BC", "CA"]

def process_file(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
            oponent, encoded_me = line.split()
            me = elementMapping[encoded_me]
            play = oponent + me
            roundValue = 0
            if oponent == me:
                roundValue +=3
            elif play in wins:
                roundValue += 6
            roundValue += element_score[me]
            result += roundValue
    return result

def process_file2(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
            roundValue = 0
            oponent, final = line.split()

            if final == "Y":
                me = oponent
                roundValue += 3
            elif final == "X":
                me = elementsLoose[oponent]
            else:
                me = enementsWin[oponent]
                roundValue += 6
            roundValue += element_score[me]
            result += roundValue
    return result

if __name__ == "__main__":
   res = process_file2(FILE_NAME)
   print(res)