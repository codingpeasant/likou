from collections import defaultdict, deque


def evaluate(input: list[str]):
    graph = defaultdict(list)
    target = input[0]
    formulas = input[1]
    for formula in formulas:
        tokens = formula.replace(" ", "").split("=")
        graph[tokens[0]].append(tokens[1])
        graph[tokens[1]].append(tokens[0])

    visited = set()

    def dfs(root: str):
        if root.isdigit():
            return int(root)
        visited.add(root)
        res = -1
        for nei in graph[root]:
            if not nei in visited:
                res = dfs(nei)
                if res != -1:
                    return res
        return res

    return dfs(target)


def evaluate1(input: list[str]):
    graph = defaultdict(list)
    numberRelation = defaultdict(list)  # list has 3 elements - left, right, sign
    target = input[0]
    formulas = input[1]
    q = deque()
    for formula in formulas:
        tokens = formula.replace(" ", "").split("=")
        if tokens[1].isdigit():
            q.append((tokens[0], int(tokens[1])))
        else:
            stringRight = tokens[1].replace(" ", "")
            if "+" in stringRight:
                tokensRight = stringRight.split("+")
                numberRelation[tokens[0]].append((tokensRight[0], tokensRight[1], 1))
                if not tokensRight[0].isdigit():
                    graph[tokens[0]].append(tokensRight[0])
                    graph[tokensRight[0]].append(tokens[0])
                if not tokensRight[1].isdigit():
                    graph[tokens[0]].append(tokensRight[1])
                    graph[tokensRight[1]].append(tokens[0])
            else:
                tokensRight = stringRight.split("-")
                numberRelation[tokens[0]].append((tokensRight[0], tokensRight[1], -1))
                if not tokensRight[0].isdigit():
                    graph[tokens[0]].append(tokensRight[0])
                    graph[tokensRight[0]].append(tokens[0])
                if not tokensRight[1].isdigit():
                    graph[tokens[0]].append(tokensRight[1])
                    graph[tokensRight[1]].append(tokens[0])

    visited = set()
    while q:
        left, right = q.popleft()
        if left == target:
            return right

        for nei in graph[left]:
            nei


input1 = ["T2", ["T1 = 1", "T2 = T3", "T3 = T1"]]
print(evaluate(input1))
input2 = ["T2", ["T1 = 1", "T2 = 2 + T4", "T3 = T1 - 4", "T4 = T1 + T3"]]
print(evaluate1(input2))
input3 = ["T2", ["T1 = 1", "T2 = 2 + T4", "T3 = T1 - 4"]]
