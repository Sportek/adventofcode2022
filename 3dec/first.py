def rucksack(path):
    with open(path) as file:
        letters = []
        for line in file:
            line = line.replace("\n", "")
            first = line[0:int(len(line) / 2)]
            second = line[int(len(line) / 2):]
            for letter in first:
                if second.count(letter) != 0:
                    print(letter)
                    index = 96
                    if letter.isupper():
                        index = 64 - 26
                    letters.append(ord(letter) - index)
                    break
        return sum(letters)


if __name__ == '__main__':
    print(rucksack("code.txt"))
