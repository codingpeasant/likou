# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort to skip the consecutive duplicate candidate
        res = []

        def backtrack(cur: List[int], cur_sum, start):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur_sum += candidates[i]
                cur.append(candidates[i])
                backtrack(
                    cur, cur_sum, i + 1
                )  # i + 1 guarantees that the next stack level doesn't pick the current candidate
                cur.pop()
                cur_sum -= candidates[i]

        backtrack([], 0, 0)
        return res


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
print(s.combinationSum2(candidates, 8))
