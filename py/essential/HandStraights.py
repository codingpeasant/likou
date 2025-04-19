# https://leetcode.com/problems/hand-of-straights/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        hand_count = Counter(hand)
        # Try to form groups of the specified size starting from the smallest card each time. Decrease the count of each card used. If at any point you cannot form a complete group, return false.
        for card in hand:
            if hand_count[card] > 0:
                for i in range(groupSize):
                    if hand_count[card + i] <= 0:
                        return False
                    hand_count[card + i] -= 1
        return True


s = Solution()
print(s.isNStraightHand([1, 2, 3, 4, 5], 4))  # False
print(s.isNStraightHand([1, 2, 3, 4, 5], 5))  # True
