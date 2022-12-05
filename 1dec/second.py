def getBestsElfs(path):
    actual_max = [-1, -1, -1]
    actual_count = 0
    with open(path) as file:
        for line in file:
            if line == "\n":
                for index, max in enumerate(actual_max):
                    if max < actual_count:
                        actual_max.insert(index, actual_count)
                        del actual_max[-1]
                        break
                actual_count = 0
                continue
            else:
                actual_count += int(line)
    return sum(actual_max)


if __name__ == '__main__':
    print(getBestsElfs("code.txt"))
