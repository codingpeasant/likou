# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # height and width of matrix
        h, w = len(matrix), len(matrix[0])

        # update prefix sum on each row
        for y in range(h):
            for x in range(1, w):
                matrix[y][x] = matrix[y][x] + matrix[y][x - 1]

        # number of submatrices that sum to target
        counter = 0

        # sliding windows on x-axis, in range [left, right]
        for left in range(w):
            for right in range(left, w):

                # accumulation of area so far
                accumulation = collections.defaultdict(int)
                accumulation[0] = 1

                # area of current submatrices, bounded by [left, right] with height y
                area = 0

                # scan each possible height on y-axis
                for y in range(h):

                    if left > 0:
                        area += matrix[y][right] - matrix[y][left - 1]

                    else:
                        area += matrix[y][right]

                    # if ( area - target ) exist, then target must exist in submatrices
                    counter += accumulation[area - target]

                    # update dictionary with current accumulation area
                    accumulation[area] = accumulation[area] + 1

        return counter


s = Solution()
matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
print(s.numSubmatrixSumTarget(matrix, 3))
