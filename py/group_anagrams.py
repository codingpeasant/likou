# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = "".join(sorted(word))  # join all chars splitted by empty string
            res[key] = res.get(key, []) + [
                word
            ]  # merge the word as a list to the existing one
        return list(res.values())


s = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(s.groupAnagrams(input))
