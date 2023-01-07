# https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if not n % 3 == 0:
            return False
        return self.isPowerOfThree(n / 3)


s = Solution()
print(s.isPowerOfThree(10))
