# https://leetcode.com/problems/lemonade-change/description/
# Neet

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        
        five_dollars = 0
        ten_dollars = 0

        for x in bills:
            if x == 5:
                five_dollars += 1
            elif x == 10:
                if five_dollars > 0:
                    five_dollars -= 1
                else:
                    return False
                ten_dollars += 1
            else: # $20
                if five_dollars > 0 and ten_dollars > 0: # $15 = $5 + $10
                    five_dollars -= 1
                    ten_dollars -= 1
                elif five_dollars > 2: # $15 = $5 + $5 + $5
                    five_dollars -= 3
                else:
                    return False
            print(five_dollars, ten_dollars)
        return True

s=Solution()
bills = [5, 5, 5, 10, 20]
print(s.lemonadeChange(bills))  # Output: True
bills = [5, 5, 10, 10, 20]
print(s.lemonadeChange(bills))  # Output: False