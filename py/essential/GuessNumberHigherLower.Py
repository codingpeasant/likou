# https://leetcode.com/problems/guess-number-higher-or-lower/
# Neet


class Solution:
    def __init__(self, answer: int) -> None:
        self.answer = answer

    def guess(self, num: int) -> int:
        if num == self.answer:
            return 0
        return -1 if num > self.answer else 1

    def guessNumber(self, n: int) -> int:

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if self.guess(mid) == 1:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution(6)
print(s.guessNumber(10))
