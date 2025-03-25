# https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


s = Solution()
print(s.subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
