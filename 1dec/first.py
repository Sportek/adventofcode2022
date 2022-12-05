def getBestElfs(path):
    actual_count = 0
    actual_max = -1
    with open(path) as file:
        for line in file:
            if line == "\n":
                if actual_max < actual_count:
                    actual_max = actual_count
                actual_count = 0
                continue
            else:
                actual_count += int(line)
    return actual_max


def another_way(path):
    list = []
    with open(path) as data:
        elf = []
        for line in data:
            if line == "\n":
                list.append(elf)
                elf = []
                continue
            else:
                line.replace("\n", "")
                elf.append(int(line))
    return sorted([sum(i) for i in list])[-1]


if __name__ == '__main__':
    print(getBestElfs("code.txt"))
    print(another_way("code.txt"))
