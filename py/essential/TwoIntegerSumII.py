# https://neetcode.io/problems/two-integer-sum-ii
# Neet

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
s = Solution()
input = [2,7,11,15]
target = 9
print(s.twoSum(input, target))