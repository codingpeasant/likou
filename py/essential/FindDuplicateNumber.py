# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find the duplicate number in an array containing n integers where each integer is between 1 and n (inclusive).
        The algorithm should run in O(n) time and use O(1) space.
        :param nums: List[int] - List of integers
        :return: int - The duplicate number
        """
        # Initialize two pointers for the cycle detection algorithm

        slow = fast = nums[0]

        # First phase: Finding the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Second phase: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
# 0 1 2 3 4
# 1 3 4 2 2
# 0 -> 1 -> 3 -> 2 <-> 4
# nums[0] is used as the starting point and is the dummy node that is not part of the cycle