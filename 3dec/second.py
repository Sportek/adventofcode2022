def rucksack(path):
    with open(path) as file:
        letters = []
        data = [[], [], []]
        counter = 0
        for line in file:
            data[counter] = line.replace("\n", "")
            counter += 1
            if counter == 3:
                counter = 0
                commons = list(set(data[0]).intersection(data[1], data[2]))
                print(commons)
                letter = commons[0]
                index = 96
                if letter.isupper():
                    index = 64 - 26
                letters.append(ord(letter) - index)
        return sum(letters)
if __name__ == '__main__':
    print(rucksack("code.txt"))