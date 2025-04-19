# https://leetcode.com/problems/contiguous-array/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count]) # don't need to update table[count] because we want the first occurrence for the longest subarray
            else:
                table[count] = index
        
        return max_length
    
s=Solution()
print(s.findMaxLength([0,1])) # 2
print(s.findMaxLength([0,1,0])) # 2
print(s.findMaxLength([0,1,0,1])) # 4
print(s.findMaxLength([0,1,0,1,0])) # 4
print(s.findMaxLength([0,1,0,1,0,0,1]))