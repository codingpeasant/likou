# https://leetcode.com/problems/product-of-array-except-self/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind
# Neet

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefixProduct, postfixProducts = [1] * (n + 1), [1] * (
            n + 1
        )  # padding with one more element to avoid index out of range
        for i in range(1, n + 1):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
        for i in range(n - 1, -1, -1):
            postfixProducts[i] = postfixProducts[i + 1] * nums[i]
        for i in range(n):
            res.append(prefixProduct[i] * postfixProducts[i + 1])
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf2([1, 2, 3, 4, 5]))  # [120,60,40,30,24]
print(s.productExceptSelf2([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
