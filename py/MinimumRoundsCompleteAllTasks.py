# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCount, res = Counter(tasks), 0
        for count in taskCount.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                res += count // 3
            if count % 3 == 1:
                res += (count - 1) // 3 + 1
            if count % 3 == 2:
                res += (count + 1) // 3
        return res


s = Solution()
tasks = [2, 3, 3]
print(s.minimumRounds(tasks))
