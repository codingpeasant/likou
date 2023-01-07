# https://leetcode.com/problems/subarray-sum-equals-k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        sum_count = {0: 1}

        for i in range(0, len(nums)):
            cur_sum += nums[i]
            if sum_count.get(cur_sum - k):
                res += sum_count[cur_sum - k]
            sum_count[cur_sum] = sum_count.get(cur_sum, 0) + 1
        return res


s = Solution()
nums = [1, 2, 3, -3]
print(s.subarraySum(nums, 3))
