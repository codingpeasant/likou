# https://leetcode.com/problems/making-a-large-island/description/

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # A dfs function to mark all the connected indices to 
        # the passed index to the value of currIslands and
        # return the number of connected indices having 1 as its value
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = currIsland
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        # counting the number of islands found
        currIsland = 0
        # this array stores the landmass of each island
        islands = [0]
        # marking and finding the landmasses of all the islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    currIsland -= 1
                    islands.append(dfs(i, j))

        maxIsland = max(islands)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # This set checks for all the unique islands 
                    # on the neighbouring four square
                    islandsAround = set()
                    if i > 0 and grid[i - 1][j] < 0:
                        islandsAround.add(grid[i - 1][j])
                    if i < n - 1 and grid[i + 1][j] < 0:
                        islandsAround.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] < 0:
                        islandsAround.add(grid[i][j - 1])
                    if j < n - 1 and grid[i][j + 1] < 0:
                        islandsAround.add(grid[i][j + 1])

                    # calculating the total landmass if this
                    # index was to be a landmass by using 
                    # previously stored landmasses of all islands
                    totalLandAround = 1
                    for k in islandsAround:
                        totalLandAround += islands[-k]
                    maxIsland = max(maxIsland, totalLandAround)
        return maxIsland
            

s=Solution()
print(s.largestIsland([[1,0],[0,1]]))