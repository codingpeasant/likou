# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/


from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        ans = 0
        while left <= right:
            val = nums[left] + nums[right]
            if val > target:
                right -= 1
            else:  # all the subsequences that start with nums[left]; nums[left+1]...nums[right] have 2**(right-left)-1 subsequences + nums[left] itself hence 2**(right-left)
                ans += pow(2, right - left, 10**9 + 7)
                left += 1
        return ans % (10**9 + 7)


s = Solution()
nums = [2, 3, 3, 4, 6, 7]
target = 12
print(s.numSubseq(nums, target))
