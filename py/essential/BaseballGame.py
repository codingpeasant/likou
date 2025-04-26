# https://leetcode.com/problems/baseball-game/description/
# Neet

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            print(scores)
            if op.lstrip("-").isdigit():
                scores.append(int(op))
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
        return sum(scores)
    
s=Solution()
print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))