# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity) -> bool:
            daysUsed = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    daysUsed += 1
                    if daysUsed > days:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left # or right because the loop exits when left == right


s = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(s.shipWithinDays(weights, days))
