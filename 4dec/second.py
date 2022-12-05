def camp_cleanup_2(path):
    with open(path) as file:
        count = 0
        for line in file:
            line.replace("\n", "")
            first = [i for i in range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)]
            second = [i for i in range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)]
            if any(item in first for item in second) or any(item in second for item in first):
                count += 1
    return count


if __name__ == '__main__':
    print(camp_cleanup_2(path="input.txt"))
