# https://leetcode.com/problems/largest-number/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sortedNums = sorted(map(str, nums), key=lambda x: x * 10, reverse=True) # * 10 because the max length of the number is 10 (10^9)
        
        result = ''.join(sortedNums)
        return result if result[0] != '0' else '0' # if the first number is 0, then all numbers are 0

s=Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))