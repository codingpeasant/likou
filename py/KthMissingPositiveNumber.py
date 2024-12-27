# https://leetcode.com/problems/kth-missing-positive-number/

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k

    def findKthPositive2(self, arr, k):
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i


s = Solution()
input = [2, 3, 4, 7, 11]
print(s.findKthPositive(input, 5))
print(s.findKthPositive2(input, 5))
