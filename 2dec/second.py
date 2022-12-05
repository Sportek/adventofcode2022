def getByValue(findVal, winning):
    winning_conditions = [["X", "Z"], ["Y", "X"], ["Z", "Y"]]
    for value in winning_conditions:
        if value[winning] == findVal:
            return value


def rockPaperCisor(path):
    myPoint = 0
    with open(path) as file:
        dict = {"X": 1, "Y": 2, "Z": 3}
        for rockPaper in file:
            rockPaper = rockPaper.replace("A", "X").replace("B", "Y").replace("C", "Z").replace("\n", "")
            first = rockPaper.split(" ")[0]
            isWinning = rockPaper.split(" ")[1]
            second = ""

            match isWinning:
                case "Z":
                    second = getByValue(first, 1)[0]
                case "Y":
                    second = first
                case "X":
                    second = getByValue(first, 0)[1]

            if second == "X" and first == "Z" or second == "Y" and first == "X" or second == "Z" and first == "Y":
                myPoint += 6
            elif second == first:
                myPoint += 3
            myPoint += dict[second]
    return myPoint


if __name__ == '__main__':
    print(rockPaperCisor("code.txt"))
