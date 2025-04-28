# https://leetcode.com/problems/split-array-largest-sum/description/
# Neet

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(mid: int) -> bool:  # greedy
            count, current_sum = 1, 0
            for num in nums:
                current_sum += num
                if (
                    current_sum > mid
                ):  # if the current sum exceeds mid, we need to split and the new subarray starts with the current number
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.splitArray([7, 2, 5, 10, 8], 2))  # 18
print(s.splitArray([1, 2, 3, 4, 5], 2))  # 9
print(s.splitArray([1, 4, 4], 3))  # 4
