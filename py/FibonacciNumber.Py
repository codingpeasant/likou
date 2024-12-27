# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        fib_list = [0] * (n + 1)
        fib_list[0] = 0
        fib_list[1] = 1

        for i in range(2, n + 1):
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        return fib_list[n]

    def fib1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib1(n - 2) + self.fib1(n - 1)


s = Solution()
print(s.fib(10))
print(s.fib1(10))
