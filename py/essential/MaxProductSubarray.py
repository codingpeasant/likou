# Blind
# Neet
# Grind
# https://leetcode.com/problems/maximum-product-subarray/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        # needs to track both min and max to find the next max or min
        dpMax, dpMin = [0] * n, [0] * n
        dpMin[0] = nums[0]
        dpMax[0] = nums[0]  # max ending here - i must be included as the ending element
        res = nums[0]
        for i in range(1, n):
            # just use the current num or a product with the previous max or min to cover the case of multiplying the previous subarray
            dpMax[i] = max(nums[i], dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i])
            dpMin[i] = min(nums[i], dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i])
            res = max(dpMax[i], res)
        return res


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
