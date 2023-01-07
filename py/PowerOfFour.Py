# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if not n % 4 == 0:
            return False
        return self.isPowerOfFour(n / 4)


s = Solution()
print(s.isPowerOfFour(5))
