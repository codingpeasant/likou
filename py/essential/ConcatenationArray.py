# https://leetcode.com/problems/concatenation-of-array/description/
# Neet

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2 # or nums + nums
    
s=Solution()
input = [1,2,1]
print(s.getConcatenation(input))