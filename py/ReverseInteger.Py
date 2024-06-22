# https://leetcode.com/problems/reverse-integer/
# Math,Simulation


class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            res = res * 10 + x % 10
            x = int(x / 10)  # or x //= x
        return res * symbol if res < pow(2, 31) else 0


s = Solution()
x = 123
print(s.reverse(x))
