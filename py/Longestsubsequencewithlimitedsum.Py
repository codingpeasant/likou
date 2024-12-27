# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums, n, m = sorted(nums), len(nums), len(queries)
        prefixSum, res = [0] * n, [0] * m
        for i, num in enumerate(nums):
            if i != 0:
                prefixSum[i] = prefixSum[i - 1] + num
            else:
                prefixSum[i] = num

        for i, query in enumerate(queries):
            if query >= prefixSum[0]:
                res[i] = bisect.bisect_right(prefixSum, query)

        return res


s = Solution()
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(s.answerQueries(nums, queries))
