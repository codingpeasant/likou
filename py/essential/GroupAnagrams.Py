# https://leetcode.com/problems/group-anagrams/
# Blind
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        for word in strs:
            wordKey = "".join(sorted(word))
            resMap[wordKey].append(word)
        return list(resMap.values())


s = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(s.groupAnagrams(input))
