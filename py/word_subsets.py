# https://leetcode.com/problems/word-subsets/

from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # construct the unique subset for B
        subset = {}  # could do [0] * 26 instead of a dict

        for b in words2:
            for (
                char
            ) in b:  # see if current count of char or previous count of char has more
                subset[char] = max(b.count(char), subset.get(char, 0))

        # now see if any words satisfy the letters in the subset
        ans = []
        for a in words1:
            # look through all the entries in the dictionary (its keys)
            # if the count in 'a' is enough to cancel out for all keys, we're golden
            if all(a.count(char) >= subset[char] for char in subset.keys()):
                ans.append(a)

        return ans


s = Solution()
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["eoo", "o", "ka"]
print(s.wordSubsets(words1, words2))
