from collections import defaultdict, deque


def evaluate(input: list[str]):
    graph = defaultdict(list)
    target = input[0]
    formulas = input[1]
    q = deque()
    for formula in formulas:
        tokens = formula.replace(" ", "").split("=")
        if tokens[1].lstrip().isdigit():
            q.append((tokens[0], tokens[1]))

        graph[tokens[0]].append(tokens[1])
        graph[tokens[1]].append(tokens[0])


    visited = set()
    while q:
        left, right = q.popleft()
        visited.add(left)
        if left == target:
            return right
        for nei in graph[left]:
            if nei not in visited:
                q.append((nei, right))
    return -1

    
def evaluate1(input: list[str]):
    graph = defaultdict(list)
    numberRelation = defaultdict(list)  # list has 3 elements - left, right, sign
    target = input[0]
    formulas = input[1]
    q = deque()
    for formula in formulas:
        tokens = formula.replace(" ", "").split("=")
        if tokens[1].isdigit():
            q.append((tokens[0], tokens[1]))
        else:
            stringRight = tokens[1].replace(" ", "")
            if "+" in stringRight:
                tokensRight = stringRight.split("+")
                numberRelation[tokens[0]] = [tokensRight[0], tokensRight[1], 1]
                if not tokensRight[0].isdigit():
                    graph[tokens[0]].append(tokensRight[0])
                    graph[tokensRight[0]].append(tokens[0])
                if not tokensRight[1].isdigit():
                    graph[tokens[0]].append(tokensRight[1])
                    graph[tokensRight[1]].append(tokens[0])
            else:
                tokensRight = stringRight.split("-")
                numberRelation[tokens[0]] = [tokensRight[0], tokensRight[1], -1]
                if not tokensRight[0].isdigit():
                    graph[tokens[0]].append(tokensRight[0])
                    graph[tokensRight[0]].append(tokens[0])
                if not tokensRight[1].isdigit():
                    graph[tokens[0]].append(tokensRight[1])
                    graph[tokensRight[1]].append(tokens[0])

    visited = set()

    while q:
        left, right = q.popleft()
        print(f"left: {left}, right: {right}")
        if left == target:
            return right

        for nei in graph[left]:
            if nei in numberRelation:
                if nei not in visited:
                    for i in range(2):
                        if numberRelation[nei][i] == left: numberRelation[nei][i] = right
                    if numberRelation[nei][0].lstrip("-").isdigit() and numberRelation[nei][1].lstrip("-").isdigit():
                        neiRes = int(numberRelation[nei][0]) + int(numberRelation[nei][1]) * numberRelation[nei][2]
                        q.append((nei, str(neiRes)))
                        visited.add(nei)
                        numberRelation.pop(nei)
    return -1
            


input1 = ["T2", ["T1 = 1", "T2 = T3", "T3 = T1"]]
print(evaluate(input1))
input2 = ["T2", ["T1 = 1", "T2 = 2 + T4", "T3 = T1 - 4", "T4 = T1 + T3"]]
print(evaluate1(input2))
input3 = ["T2", ["T1 = 1", "T2 = 2 + T4", "T3 = T1 - 4"]]
print(evaluate1(input3))