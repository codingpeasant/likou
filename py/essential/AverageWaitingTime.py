# https://leetcode.com/problems/average-waiting-time/description/

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total, time = (
            customers[0][1],
            customers[0][0] + customers[0][1],
        )

        for i in range(1, len(customers)):
            if customers[i][0] < time:
                total += time - customers[i][0]
                time += customers[i][1]
            else:
                time = customers[i][0] + customers[i][1]
            total += customers[i][1]
        return total / len(customers)


s = Solution()
print(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
