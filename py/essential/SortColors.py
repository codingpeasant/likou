# https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=rab78cw1
# Grind


from collections import Counter, defaultdict


class Solution:
    def sortColors(self, nums):
        colorCounter = Counter(nums)
        index = 0
        for i in range(3): # lay each color from 0 to 2 back to the array based on the counter for each color
            while colorCounter[i] > 0:
                nums[index] = i
                index += 1
                colorCounter[i] -= 1


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
