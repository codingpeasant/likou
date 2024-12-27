# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import defaultdict, deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque()
        queue.append(start)
        bankSet = set(bank)
        step = 0

        while queue:
            count = len(queue)
            for _ in range(count):
                cur = queue.popleft()
                if cur == end:
                    return step

                for i in range(len(cur)):  # 8 * 4 per cur
                    for c in "AGCT":
                        mutation = cur[:i] + c + cur[i + 1 :]
                        if mutation in bankSet:
                            bankSet.remove(mutation)
                            queue.append(mutation)
            step += 1

        return -1


s = Solution()
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(s.minMutation(start, end, bank))
