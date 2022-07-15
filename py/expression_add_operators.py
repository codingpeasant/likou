# https://leetcode.com/problems/expression-add-operators/

from turtle import back
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(pos, path, result_so_far, prev_value):
            if pos == len(num):
                if result_so_far == target:
                    res.append(path)
                return
            for i in range(pos, len(num)):
                if i > pos and num[pos] == "0":
                    break  # skip leading zero number. e.g. 1,02
                cur = int(num[pos : i + 1])
                if pos == 0:
                    backtrack(i + 1, path + str(cur), cur, cur)
                else:
                    backtrack(i + 1, path + "+" + str(cur), result_so_far + cur, cur)
                    backtrack(i + 1, path + "-" + str(cur), result_so_far - cur, -cur)
                    backtrack(
                        i + 1,
                        path + "*" + str(cur),
                        result_so_far - prev_value + prev_value * cur,
                        prev_value * cur,
                    )  # going backward and re-eval. e.g. 2+3*2: result_so_far = 5 (2+3); prev_value = 3; eval = 5 - 3 + 3 * 2

        backtrack(0, "", 0, 0)
        return res


s = Solution()
num, target = "105", 5
print(s.addOperators(num, target))
