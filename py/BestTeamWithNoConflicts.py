# https://leetcode.com/problems/best-team-with-no-conflicts/description/

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #   Example: scores = [4,4,6,5]
        #              ages = [2,1,5,1]

        dp = [0] * (1 + max(ages))  #         dp = [0, 0, 0, 0, 0]
        #  score_age = [(4,1), (4,2), (5,1), (6,5)]
        score_age = sorted(zip(scores, ages))
        #   score   age     dp
        for score, age in score_age:  #   –––––  –––––    ––––––––––––––––––
            #     4      1      [0, 4, 0, 0, 0, 0]
            dp[age] = score + max(dp[: age + 1])  #     4      2      [0, 4, 8, 0, 0, 0]
            #     5      1      [0, 9, 8, 0, 0, 0]
        return max(dp)  #     6      5      [0, 9, 8, 0, 0,15]
        #                                   |
        #                                 return

    def bestTeamScore1(self, scores: List[int], ages: List[int]) -> int:
        ageScorePair, n = sorted(zip(ages, scores)), len(scores)
        # dp[i] stores the maximum score that can be obtained when i-th player is included and all other players are between indices 0 and i-1.
        dp = [ageScorePair[i][1] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if ageScorePair[i][1] >= ageScorePair[j][1]:
                    dp[i] = max(dp[i], ageScorePair[i][1] + dp[j]) # pick i only or join i to the previous smaller players (subsequence)

        return max(dp)


s = Solution()
scores = [4, 5, 6, 5]
ages = [2, 1, 2, 1]
print(s.bestTeamScore(scores, ages))
print(s.bestTeamScore1(scores, ages))
