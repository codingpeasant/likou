# https://leetcode.com/problems/subsets-ii/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start: int, curList: List[int]):
            res.append(curList)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, curList + [nums[i]])

        backtrack(0, [])
        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(s.subsetsWithDup([0]))  # [[],[0]]
print(
    s.subsetsWithDup([4, 4, 4, 1, 4])
)  # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
