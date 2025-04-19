# https://leetcode.com/problems/swim-in-rising-water/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Binary search on the answer.
        The answer is in the range [0, max(grid)].
        We can use BFS to check if we can reach the bottom right corner (n-1, n-1) from the top left corner (0, 0)
        with the given time limit.
        You can also use Dijkstra's algorithm to find the shortest path in a weighted graph. Because in order to minimize the time, we need to find the path with the minimum maximum height so that we can pass it and reach the destination.
        """
        n = len(grid)
        l, r = 0, max(max(row) for row in grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def can_swim_in_time_bfs(time: int) -> bool:
            if grid[0][0] > time or grid[n - 1][n - 1] > time:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            queue = [(0, 0)]


            while queue:
                x, y = queue.pop(0)
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= time:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        
        def can_swim_in_time_dfs(time: int, i: int, j: int, visited: set) -> bool:
            if i == n - 1 and j == n - 1:
                return True
            if grid[0][0] > time or grid[n - 1][n - 1] > time:
                return False
            visited.add((i, j))
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited and grid[ni][nj] <= time:
                    visited.add((ni, nj))
                    if can_swim_in_time_dfs(time, ni, nj, visited=visited):
                        return True
            return False

        while l < r:
            mid = (l + r) // 2
            if can_swim_in_time_dfs(mid, 0, 0, set()):
                r = mid
            else:
                l = mid + 1

        return l

s = Solution()
print(s.swimInWater([[0,2],[1,3]]))  # 3
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # 16