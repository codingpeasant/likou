# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Neet

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:  ## array is None so element can't be found
            return False

        low = 0
        high = len(nums) - 1  ## initialise the low and the high variables for BS

        while low < high:

            mid = (low + high) // 2

            if nums[mid] == target or nums[low] == target or nums[high] == target:
                return (
                    True  ## checking for a match of target on each of the three pointer
                )

            if nums[mid] < nums[high]:

                """
                consider the case of [2,5,6,0,0,1,2] and target = 1
                Here high = 6, low = 0 and mid = 3.
                so nums[mid]<nums[high]
                """
                ## now we should check whether the target lies between
                ## mid and high or not. If yes, then shift low to the value next to mid.
                if nums[mid] < target <= nums[high]:

                    low = mid + 1

                else:
                    ## otherwise the value should be in the previous part.
                    ## Consider the value of target = 5 in the above example to understand better.
                    high = mid - 1

            elif nums[mid] > nums[high]:
                """
                To understand this part, consider the following case:
                nums = [0,0,1,1,2,0] and target = 0
                low = 0, high = 5 and mid = 2
                nums[mid]>nums[high]
                """

                if nums[low] <= target < nums[mid]:
                    ## if the value of target is in between low and high, the shift high to mid-1.
                    ## Like in the example above

                    high = mid - 1
                else:
                    ## Otherwise shift the value of low to mid +1.
                    ## Consider target =2 in the above example to understand better.
                    low = mid + 1

            else:
                """
                This will execute when nums[mid] and nums[high] are same.
                For e.g:
                nums=[2,2,2,2,3,4,5,2] and target = 4
                here, low = 0, high = 7 and mid = 3
                nums[mid] = nums[high] and thus we can't be certain about which direction to go.
                But one thing is sure, the value is definitely not at the high position.
                So just decrease the value of high pointer

                """

                high -= 1

        if nums[low] == target:
            return True

        return False


s = Solution()
print(s.search([2, 5, 6, 0, 0, 1, 2], 0))  # True
print(s.search([2, 5, 6, 0, 0, 1, 2], 3))  # False
print(s.search([1, 0, 1, 1, 1], 0))  # True
