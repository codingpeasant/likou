# Blind
# Grind
# Neet
# https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, sortedNums = [], sorted(nums)
        for i in range(len(nums) - 2):
            if i == 0 or (
                i > 0 and sortedNums[i] != sortedNums[i - 1]
            ):  # skip the same result - you have to calculate anyway when i == 0
                left, right, sumToMake = i + 1, len(sortedNums) - 1, -sortedNums[i]
                while left < right:
                    if sumToMake == sortedNums[left] + sortedNums[right]:
                        res.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                        while (
                            left < right and sortedNums[left] == sortedNums[left + 1]
                        ):  # skip same result
                            left += 1
                        while (
                            left < right and sortedNums[right] == sortedNums[right - 1]
                        ):
                            right -= 1
                        left += 1
                        right -= 1
                    elif sumToMake > sortedNums[left] + sortedNums[right]:
                        left += 1
                    else:
                        right -= 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 10, 2, -1, -4]))
