# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCount = Counter(t)
        left = 0
        minWindow = ""
        targetLen = len(t)

        for right in range(len(s)):
            if targetCount[s[right]] > 0:  # found a needed letter
                targetLen -= 1

            targetCount[s[right]] -= 1
            while targetLen == 0:  # all needed letters are included
                windowLen = right - left + 1

                if not minWindow or windowLen < len(
                    minWindow
                ):  # first time reach target or found a shorter one
                    minWindow = s[left : right + 1]

                targetCount[s[left]] += 1
                if targetCount[s[left]] > 0:  # start is in t and is needed
                    targetLen += 1
                left += 1

        return minWindow


so = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(so.minWindow(s, t))
