# https://leetcode.com/problems/valid-anagram/


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_map = collections.defaultdict(int)
        for letter in s:
            letter_map[letter] += 1
        for letter in t:
            letter_map[letter] -= 1

        return all(x == 0 for x in letter_map.values())


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
