# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = Counter(t)
        start, end = 0, 0
        min_window = ""
        target_len = len(t)

        for end in range(len(s)):
            if target_count[s[end]] > 0:  # found a needed letter
                target_len -= 1

            target_count[s[end]] -= 1
            while target_len == 0:  # all needed letters are included
                window_len = end - start + 1

                if not min_window or window_len < len(min_window):
                    min_window = s[start : end + 1]

                target_count[s[start]] += 1
                if target_count[s[start]] > 0:  # start is in t and is needed
                    target_len += 1
                start += 1

        return min_window


so = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(so.minWindow(s, t))
