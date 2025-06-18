# https://leetcode.com/problems/most-profit-assigning-work/description/

from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        diffPro = sorted(zip(difficulty, profit), key=lambda x: -x[1])
        worker.sort(reverse=True)
        profitP = 0
        res = 0
        for wo in worker:
            while profitP < len(diffPro) and diffPro[profitP][0] > wo:
                profitP += 1
            if profitP < len(diffPro):
                res += diffPro[profitP][1]
        return res


s = Solution()
print(s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
print(s.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
