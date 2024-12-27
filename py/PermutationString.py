# https://leetcode.com/problems/permutation-in-string/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCount, left = Counter(s1), 0
        for right, char in enumerate(s2):
            charCount[char] -= 1  # Counter returns defaultdict(int)
            while (
                charCount[char] < 0
            ):  # If number of characters `c` is more than our expectation; c could be any char
                charCount[s2[left]] += 1  # Slide left until charCount[c] == 0
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False


s = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(s.checkInclusion(s1, s2))
