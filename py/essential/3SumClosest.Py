# https://leetcode.com/problems/3sum-closest/
# Sorting,Two Pointers
# Grind
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        # pin the first number
        for i in range(len(nums) - 2):
            if nums[i - 1] == nums[i] and i != 0:
                continue
            # search the numbers after the pinned number
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                if cur_sum == target:
                    return target

                if abs(target - res) > abs(target - cur_sum):
                    res = cur_sum

                if target > cur_sum:  # too small, needs to try bigger possible numbers
                    left += 1
                if target < cur_sum:
                    right -= 1
        return res


s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
