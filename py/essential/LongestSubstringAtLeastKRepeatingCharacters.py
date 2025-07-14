# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == [] or k > len(s):
            return 0
        freq = collections.Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(
                    self.longestSubstring(s[:i], k),
                    self.longestSubstring(s[i + 1 :], k),
                )
        return len(s)


s = Solution()
print(s.longestSubstring("ababbc", 2))
