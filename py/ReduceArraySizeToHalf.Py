# https://leetcode.com/problems/reduce-array-size-to-the-half

from typing import Counter, List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        freq = sorted(cnt.values())

        res, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            removed += freq.pop()  # greedy
            res += 1
        return res


s = Solution()
input = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(s.minSetSize(input))
