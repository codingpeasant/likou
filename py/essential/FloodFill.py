# https://leetcode.com/problems/flood-fill/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if (
                x < 0
                or y < 0
                or x > m - 1
                or y > n - 1
                or image[x][y] != start_color
                or image[x][y] == color
            ):
                return
            image[x][y] = color
            for nextX, nextY in dirs:
                dfs(x + nextX, y + nextY)

        dfs(sr, sc)
        return image


s = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(s.floodFill(image, sr, sc, newColor))
