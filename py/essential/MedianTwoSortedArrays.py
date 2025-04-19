# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4070371/94-96-binary-search-two-pointers/?envType=problem-list-v2&envId=rr2ss0g5
# Neet
# Grind

from typing import List


class Solution:
    # to find the median, you need to find the partition of the two arrays such that the left partition is smaller than the right partition
    # and the number of elements in the left partition is equal to the number of elements in the right partition
    # we can use binary search to find the partition
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array to run the binary search on to save a bit of time
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m # low has to be 0 because the length can be 0

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (
                m + n + 1
            ) // 2 - partitionX  # partitionY + partitionX should be half of the total length of the two arrays so we can calculate the partitionY based on partitionX

            # Handling edge cases where partition is at 0 or end
            maxX = (
                float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            )  # max value of left partition of nums1
            maxY = (
                float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            )  # max value of left partition of nums2
            minX = (
                float("inf") if partitionX == m else nums1[partitionX]
            )  # min value of right partition of nums1
            minY = (
                float("inf") if partitionY == n else nums2[partitionY]
            )  # min value of right partition of nums2

            # check if everything on the left side of partitionX is smaller than everything on the right side of partitionY and vice versa
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1


s = Solution()
nums1 = [1, 2, 5]
nums2 = [3, 4, 6, 7]
print(s.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 2]
nums2 = [3, 4]
print(s.findMedianSortedArrays(nums1, nums2))
