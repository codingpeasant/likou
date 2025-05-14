# https://leetcode.com/problems/dota2-senate/description/
# Neet

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d: # r can ban d
                radiant.append(r + n) # keep the order of the index for the next round - n can be larger than n
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"

s=Solution()
senate = "RD"
print(s.predictPartyVictory(senate))  # Output: "Radiant"
senate = "RDD"
print(s.predictPartyVictory(senate))  # Output: "Dire"
senate = "RRRDD"
print(s.predictPartyVictory(senate))  # Output: "Radiant"