# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?orderBy=most_votes


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:n] == needle:
                return i
        return -1


s = Solution()
haystack = "sadbutsad"
needle = "sad"
print(s.strStr(haystack, needle))
