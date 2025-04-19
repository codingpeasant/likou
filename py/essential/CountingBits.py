# https://leetcode.com/problems/counting-bits/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet

from typing import List


class Solution:
    # Dynamic Programming with Bit Manipulation
    # The idea here is to use the number of 1's in i >> 1 (i.e., i divided by 2) and the last bit in i to find the number of 1's in i.
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1) # if last bit is 1, add 1 to the count
        return ans
    def countBits1(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = bin(i).count('1')
        return ans


s = Solution()
print(s.countBits1(5))
print(s.countBits(5))