# https://leetcode.com/problems/jump-game-iv/description/

import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nei = collections.defaultdict(list)
        for i, el in enumerate(arr):
            nei[el].append(i)

        q = collections.deque([(0, 0)])
        num_met, pos_met = set(), set()
        while q:
            pos, step = q.popleft()  # state: position, step
            if pos == len(arr) - 1:
                return step
            num = arr[pos]
            pos_met.add(pos)  # track explored positions

            next_pos = nei[num] if num not in num_met else []
            next_pos += [pos - 1, pos + 1]
            for p in next_pos:
                if p in pos_met or not 0 <= p < len(arr):
                    continue
                q.append((p, step + 1))

            num_met.add(num)  # track explored values


s = Solution()
arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
print(s.minJumps(arr))
