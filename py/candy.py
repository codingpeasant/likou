# https://leetcode.com/problems/candy/

from typing import List


class Solution:
    def candy(self, R):
        n, ans = len(R), [1] * len(R)  # assign one candy to each person

        for i in range(n - 1):
            if R[i] < R[i + 1]:
                ans[i + 1] = 1 + ans[i]

        for i in range(n - 2, -1, -1):
            if R[i + 1] < R[i]:
                ans[i] = max(1 + ans[i + 1], ans[i])

        print(ans)
        return sum(ans)


s = Solution()
input = [-1, 0, 2, 0, 3]
print(s.candy(input))
