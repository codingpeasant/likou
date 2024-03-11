# https://leetcode.com/problems/similar-string-groups/description/

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        group = 0
        visited = set()

        def similar(A, B):
            diff = 0
            for i in range(len(B)):
                if A[i] != B[i]:
                    diff += 1
                if diff > 2:
                    return False
            return True

        def dfs(string):
            for i in range(len(strs)):
                if strs[i] in visited:
                    continue
                if similar(strs[i], string):
                    visited.add(strs[i])
                    dfs(strs[i])

        for string in strs:
            if string in visited:
                continue
            visited.add(string)
            dfs(string)
            group += 1
        return group


s = Solution()
strs = ["tars", "rats", "arts", "star"]
print(s.numSimilarGroups(strs))
