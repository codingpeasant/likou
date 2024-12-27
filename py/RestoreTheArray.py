# https://leetcode.com/problems/restore-the-array/description/
# DP,Back Track

from functools import lru_cache

# Use DP to record number of valid ways end with index i, then dp[-1] is the answer.

# For an index i, we need to find out all the numbers end with s[i] and is no larger than k,
# so we traverse backward and add previous digits s[j] (j < i and j >= 0) to current s[i], until this current number is larger than k.

# For example, in array s = [1, 3, 2, 7], t = 40, for digit s[3] = 7, we find that 7, 27 are valid number.

# If we choose 7, then we have dp[2] (the number of ways end with 2) of ways to reach this end number.
# If we choose 27, then we have dp[1] (the number of ways end with 3) of ways to reach this end number.
# Then dp[3] = dp[2] + dp[1], so on so forth, until we have dp[-1].


class Solution:
    def numberOfArrays(self, s, k):
        n, mod = len(s), 10**9 + 7

        @lru_cache(None)
        def dfs(i):
            if i == 0:  # a single letter is always a valid number given 1 <= k <= 10**9
                return 1
            total = 0

            for j in range(i - 1, -1, -1):
                if s[j] == "0":  # s[j:i] is leading 0 number that is invalid
                    continue
                elif int(s[j:i]) <= k:
                    total += dfs(j) % mod
                elif (
                    int(s[j:i]) > k
                ):  # already larger than k there is no reason to move j any more
                    break

            return total

        return dfs(n) % mod

    # TLE
    def numberOfArrays1(self, s, k):
        res, n = [], len(s)

        def dfs(start: int, curList: list[int]):
            if start > n - 1:
                res.append(curList.copy())
                return
            if s[start] == "0":
                return
            for i in range(start, n):
                if int(s[start : i + 1]) <= k:
                    curList.append(int(s[start : i + 1]))
                    dfs(i + 1, curList)
                    curList.pop()
                else:
                    break

        dfs(0, [])
        print(res)
        return len(res)


s = Solution()
input = "1317"
k = 2000
print(s.numberOfArrays(input, k))
print(s.numberOfArrays1(input, k))
