# https://leetcode.ca/2016-09-16-291-Word-Pattern-II/


class Solution:
    def wordPatternMatch(self, pattern, s):
        def dfs(i, j):
            if i == m and j == n:
                return True
            if i == m and j < n:
                return False
            if j == n and i < m:
                return False
            for k in range(j, n):
                t = s[j : k + 1]
                if pattern[i] in d and d[pattern[i]] == t:
                    if dfs(i + 1, k + 1):
                        return True
                elif pattern[i] not in d and t not in vis:
                    d[pattern[i]] = t
                    vis.add(t)
                    if dfs(i + 1, k + 1):
                        return True
                    d.pop(pattern[i])
                    vis.remove(t)
            return False

        m, n = len(pattern), len(s)
        d = {}
        vis = set()
        return dfs(0, 0)


so = Solution()
pattern = "abab"
s = "redblueredblue"
print(so.wordPatternMatch(pattern, s))
