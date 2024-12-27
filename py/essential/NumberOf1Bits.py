# https://leetcode.com/problems/number-of-1-bits/description/?envType=problem-list-v2&envId=oizxjoit
# Blind


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += n & 1
            n >>= 1
        return res


s = Solution()
print(s.hammingWeight(20))
