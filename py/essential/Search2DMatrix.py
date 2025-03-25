# https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            midValue = matrix[mid // n][mid % n]
            if midValue == target:
                return True
            elif midValue < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
