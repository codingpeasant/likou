# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [1,2]
print(s.twoSum([2, 3, 4], 6))  # [1,2]
