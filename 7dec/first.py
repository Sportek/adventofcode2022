def accessToPath(dictionnary: [{}], path: list[str]):
    now_dictionnary = dictionnary[path[0]]
    path.pop(0)
    if len(path) >= 1:
        return accessToPath(now_dictionnary, path)
    else:
        return now_dictionnary


def no_space(path):
    # Donc le format des folders: {"name": "NAME", type: "folder", size: 0, contains: []}
    # Format des fichiers: {"name": "NAME", type: "file", size: 8, contains: []}
    values = [{"/": []}]
    actually_in = ["/"]

    with open(path) as file:
        for line in file:
            line = line.replace("\n", "")
            if line.startswith("$"):
                if line.startswith("$ ls"):

                elif line.startswith("$ cd .."):

                else:
                    value = line.split(" ")
                    if
                        values.append()


if __name__ == '__main__':
    no_space("input.txt")
