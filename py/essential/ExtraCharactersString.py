# https://leetcode.com/problems/extra-characters-in-a-string/description/
# Neet

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val = len(s) + 1
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0
        dictionary_set = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = (
                dp[i - 1] + 1
            )  # start with assuming there is not better case than this

            for l in range(1, i + 1):
                if s[i - l : i] in dictionary_set:
                    dp[i] = min(dp[i], dp[i - l]) # state transferring

        return dp[-1]


s = Solution()
print(s.minExtraChar("sayhelloworld", ["hello", "world"]))
