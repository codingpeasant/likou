# https://leetcode.com/problems/palindromic-substrings/description/?envType=problem-list-v2&envId=oizxjoit
# Blind


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def expandCount(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                self.res += 1

        for i in range(len(s)):
            expandCount(i, i)
            expandCount(i, i + 1)

        return self.res


s = Solution()
print(s.countSubstrings("aaa"))
