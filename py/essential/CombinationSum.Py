# https://leetcode.com/problems/combination-sum/
# Blind
# Neet

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(
            cur: List[int], cur_sum, start
        ):  # use start to not repeat previous cases e.g. [2,3,5] - [3,5] and [5,3] are the same
            if cur_sum == target:
                res.append(cur.copy())  # same with new ArrayList<Integer> in java ;)
                return

            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                backtrack(cur, cur_sum + candidates[i], i)
                cur.pop()

        backtrack([], 0, 0)

        return res


s = Solution()
candidates = [1, 2, 3]
print(s.combinationSum(candidates=candidates, target=4))
