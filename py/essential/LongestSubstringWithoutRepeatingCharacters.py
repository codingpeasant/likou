from collections import defaultdict

# Blind
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=oizxjoit


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        charCount = defaultdict(int)
        res = 0
        while right < len(s):
            charCount[s[right]] += 1
            if charCount[s[right]] == 1:
                res = max(res, right - left + 1)

            while charCount[s[right]] > 1:
                charCount[s[left]] -= 1
                left += 1
            right += 1

        return res


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
