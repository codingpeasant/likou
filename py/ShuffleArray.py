# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums) // 2):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


s = Solution()
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(s.shuffle(nums, n))
