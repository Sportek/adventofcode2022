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


if __name__ == '__main__':
    print(getBestElfs("code.txt"))
