def tuningTrouble(path):
    with open(path) as file:
        char_list = []
        line = file.readline()
        for index, char in enumerate(line):
            if len(char_list) < 14:
                char_list.append(char)
            elif len(char_list) == 14:
                char_list.pop(0)
                char_list.append(char)
                if len(set(char_list)) == len(char_list):
                    return index + 1


if __name__ == '__main__':
    print(tuningTrouble(path="input.txt"))
