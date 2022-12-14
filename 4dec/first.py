def camp_cleanup_1(path):
    with open(path) as file:
        count = 0
        for line in file:
            line.replace("\n", "")
            first = [i for i in range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)]
            second = [i for i in range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)]
            if all(item in first for item in second) or all(item in second for item in first):
                count += 1
    return count


if __name__ == '__main__':
    print(camp_cleanup_1(path="input.txt"))
