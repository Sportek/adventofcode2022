import numpy as np


def supplystakcs(path):
    important_lines = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    matrice = []
    actions = []
    with open(path) as file:
        for line in file:
            line.replace("\n", "")
            if line.startswith(" 1"):
                continue
            elif line.startswith("move"):
                numbers = (int(line.split(" ")[1]), int(line.split(" ")[3]) - 1, int(line.split(" ")[5]) - 1)
                actions.append(numbers)
            elif line == "\n":
                continue
            else:
                matrice_line = []
                for number in important_lines:
                    check = ''
                    if len(line) - 1 >= number:
                        check = line[number] if line[number] != " " else ''
                    matrice_line.append(check)
                matrice.append(matrice_line)
    matrice = np.array(matrice).transpose().tolist()
    matrice = list(filter(None, [list(filter(None, m)) for m in matrice]))

    for action in actions:
        for _ in range(action[0]):
            element_to_add = matrice[action[1]][0]
            matrice[action[2]].insert(0, element_to_add)
            del matrice[action[1]][0]
    return ''.join([element[0] for element in matrice])


if __name__ == '__main__':
    print(supplystakcs("code.txt"))
