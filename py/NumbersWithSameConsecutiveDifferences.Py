# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def dfs(cur_num):
            if len(str(cur_num)) == n:
                res.append(cur_num)
            else:
                digit_1 = cur_num % 10 - k
                digit_2 = cur_num % 10 + k
                if digit_1 >= 0:
                    dfs(cur_num * 10 + digit_1)
                if digit_2 != digit_1 and digit_2 < 10:
                    dfs(cur_num * 10 + digit_2)

        for i in range(1, 10):
            dfs(i)

        return res


s = Solution()
print(s.numsSameConsecDiff(2, 1))
