# https://leetcode.com/problems/minimum-number-of-refueling-stops/

# dp[t] means the furthest distance that we can get with t times of refueling.

# So for every station s[i],
# if the current distance dp[t] >= s[i][0], we can refuel:
# dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])

# In the end, we'll return the first t with dp[t] >= target,
# otherwise we'll return -1.
class Solution:
    def minRefuelStops(self, target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i, -1, -1):
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(
                        dp[t + 1], dp[t] + s[i][1]
                    )  # try to add fuel at i and see if it could increase the previous distance
        for t, d in enumerate(dp):
            if d >= target:
                return t
        return -1


s = Solution()
target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]

print(s.minRefuelStops(target, startFuel, stations))
