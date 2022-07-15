# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq
from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]  # [5 -> [0,2], 6 -> [1]...]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, count in counts.items():
            freq[count].append(num)

        res: List[int] = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        heap = []
        for i in freq_table.keys():
            heapq.heappush(heap, (-freq_table[i], i))  # - is for building a max heap
        ans = []
        while k > 0:
            k -= 1
            val = heapq.heappop(heap)
            ans.append(val[1])
        return ans


s = Solution()
logs = [1, 1, 1, 2, 2, 3]
print(s.topKFrequent(nums=logs, k=2))
print(s.topKFrequent1(nums=logs, k=2))
