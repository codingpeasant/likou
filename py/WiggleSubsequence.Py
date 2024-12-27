# https://leetcode.com/problems/wiggle-subsequence/
# DP

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # dp_low[i] is the longest wiggle subsequence of nums[0..i] which has the last element is in the low position. The other way around for dp_high[i]
        dp_low = [1] * n
        dp_high = [1] * n

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                # dp_high[i] will benefit from adding 1 to the current longest ending as low position
                dp_high[i] = dp_low[i - 1] + 1
                dp_low[i] = dp_low[i - 1]
            elif nums[i - 1] > nums[i]:
                dp_low[i] = dp_high[i - 1] + 1
                dp_high[i] = dp_high[i - 1]
            else:
                dp_low[i] = dp_low[i - 1]
                dp_high[i] = dp_high[i - 1]
        return max(dp_high[n - 1], dp_low[n - 1])


s = Solution()
input = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(s.wiggleMaxLength(input))
