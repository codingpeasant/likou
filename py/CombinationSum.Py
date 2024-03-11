# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur: List[int], cur_sum, start):
            if cur_sum == target:
                res.append(cur.copy())  # same with new ArrayList<Integer> in java ;)
                return

            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                cur_sum += candidates[i]
                cur.append(candidates[i])
                backtrack(cur, cur_sum, i)
                cur.pop()
                cur_sum -= candidates[i]

        backtrack([], 0, 0)

        return res


s = Solution()
candidates = [1, 2, 3]
print(s.combinationSum(candidates=candidates, target=4))
