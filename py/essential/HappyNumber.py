# https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet


class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquareSum(input: int) -> int:
            squareSum = 0
            while input > 0:
                squareSum += (input % 10) ** 2
                input = input // 10
            return squareSum

        inLoop = set()
        inLoop.add(n)
        while True:
            squareSum = getSquareSum(n)
            if squareSum == 1:
                return True
            # it loops endlessly in a cycle so dup appears
            if squareSum in inLoop:
                return False
            inLoop.add(squareSum)
            n = squareSum


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
print(s.isHappy(1))
