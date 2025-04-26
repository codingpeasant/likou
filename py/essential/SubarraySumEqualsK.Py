# https://leetcode.com/problems/subarray-sum-equals-k
# Hash Table,Prefix Sum
# Grind
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1  # for first cur_sum = k

        for num in nums:
            cur_sum += num
            if sum_count:
                res += sum_count[
                    cur_sum - k
                ]  # plus all the sub arrays that reached cur_sum - k
            sum_count[cur_sum] += 1
        return res


s = Solution()
nums = [1, 2, 3, -3, 3]
print(s.subarraySum(nums, 3))
nums = [1, 2, 3, -2]
print(s.subarraySum(nums, 3))