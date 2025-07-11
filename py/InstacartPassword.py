with open("./py/test.txt") as file:
    password = [""] * 199

    while True:
        firstLine = file.readline().strip()
        if not firstLine:
            break

        index = int(firstLine)
        if password[index]:
            break
        coordinateLine = file.readline().strip(" []\n").split(",")
        x, y = int(coordinateLine[0]), int(coordinateLine[1])
        matrix = []

        while True:
            line = file.readline()
            if not line or line == "\n":
                break
            matrix.append(line.strip())
        print(matrix)
        m, n = len(matrix), len(matrix[0])
        password[index] = matrix[m - y - 1][x]  # 2, 3 -> 0 ,2
    print("".join([letter for letter in password if letter]))
