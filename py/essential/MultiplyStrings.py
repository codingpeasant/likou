# https://leetcode.com/problems/multiply-strings/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def decode(num) -> int:
            ans = 0
            for i in num:
                ans = ans * 10 + (ord(i) - ord("0"))
            return ans

        def encode(s) -> str:
            news = ""
            while s:
                a = s % 10
                s = s // 10
                news = chr(ord("0") + a) + news
            return news

        return encode(decode(num1) * decode(num2))


s = Solution()
print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
print(s.multiply("0", "123"))
