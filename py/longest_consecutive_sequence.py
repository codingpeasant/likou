# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        res = 1

        for num in nums:
            if num in nums_set:
                count = 1
                num_next = num + 1
                while num_next in nums_set:
                    nums_set.remove(num_next)
                    count += 1
                    num_next += 1

                num_next = num - 1
                while num_next in nums_set:
                    nums_set.remove(num_next)
                    count += 1
                    num_next -= 1
                res = max(res, count)
        return res


s = Solution()
input = [100, 4, 200, 1, 3, 2, 1, 99, 101, 98, 97, 96]
print(s.longestConsecutive(input))
