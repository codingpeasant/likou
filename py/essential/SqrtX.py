# https://leetcode.com/problems/sqrtx/description/
# Neet


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


s = Solution()
print(s.mySqrt(2))
print(s.mySqrt(8))
print(s.mySqrt(4))
print(s.mySqrt(0))
print(s.mySqrt(1))
print(s.mySqrt(6))
