# https://leetcode.com/problems/find-k-closest-elements/

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        left, right = 0, len(arr) - 1

        while right - left >= k: # exclude the further numbers until there are k left
            if abs(arr[right] - x) >= abs(arr[left] - x):
                right -= 1
            else:
                left += 1
        return arr[left : right + 1]


s = Solution()
arr = [1, 1, 1, 4, 5]
k = 4
x = 3
print(s.findClosestElements(arr, k, x))
