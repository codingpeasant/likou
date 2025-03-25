# https://leetcode.com/problems/powx-n/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet


class Solution:
    # x^n = x^(n/2) * x^(n/2) if n is even
    # x^n = x^(n//2) * x^(n//2) * x if n is odd
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res

    # recursive - easier to understand
    def myPow1(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.myPow1(x * x, n // 2)
        return x * self.myPow1(x * x, n // 2)


s = Solution()
print(s.myPow(2.00000, -3))
print(s.myPow1(2.00000, -3))
