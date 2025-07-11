# https://www.1point3acres.com/bbs/thread-773559-1-1.html


def indexOf(originalStr: str, input: str):
    m, n = len(originalStr), len(input)
    if n == 0:
        return [0]
    res = []
    for i in range(m - n + 1):
        curStr = originalStr[i : i + n]
        if curStr == input:
            res.append(i)
    return res


def indexOfWithStar(originalStr: str, input: str) -> int:
    m = len(originalStr)
    tokens = input.split("*")
    n = len(tokens)
    i = 0
    j = 0
    res = -1
    while i < m and j < n:
        if originalStr[i:].startswith(tokens[j]):
            res = i if res == -1 else res
            i += len(tokens[j]) - 1
            j += 1
        i += 1
    if j == n:
        return res
    return -1


print(indexOf("abcdef", "cdf"))
print(indexOf("abcdef", "cde"))
print(indexOfWithStar("abcdef", "bc*e"))
print(indexOfWithStar("abcdef", "*c"))
print(indexOfWithStar("abcdef", "*"))
print(indexOfWithStar("abcdef", "*333"))
print(indexOfWithStar("abcdef", "cde"))

print("a".startswith("*ab".split("*")[0]))
