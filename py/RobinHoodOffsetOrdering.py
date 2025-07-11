# https://leetcode.com/discuss/post/3158526/offset-ordering-by-anonymous_user-l6gs/


def commitOffset(input: list[int]):
    res = []
    nextToExpect = 0
    alreadySeen = set()

    for offset in input:
        alreadySeen.add(offset)
        if offset == nextToExpect:
            while nextToExpect in alreadySeen:
                alreadySeen.remove(nextToExpect)
                nextToExpect += 1
            res.append(nextToExpect - 1)
        else:
            res.append(-1)

    return res


input = [2, 1, 0, 5, 4]
print(commitOffset(input))

input = [2, 0, 1]
print(commitOffset(input))
