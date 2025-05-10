# https://leetcode.com/problems/course-schedule-iv/description/
# Neet


from typing import List


class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build the adjacency list representation of the graph
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(node, visited, start):
            # Mark the current node as visited
            visited[node] = True

            # Add the pair (start, node) to the set if start != -1
            if start != -1:
                prerequisites.add((start, node))

            # Explore all neighbors of the current node
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, start)

        # Step 2: Use DFS to compute all prerequisites
        prerequisites = set()
        for i in range(numCourses):
            visited = [False] * numCourses  # Reset visited array for each node
            dfs(i, visited, i)

        # Step 3: Answer each query
        return [(query[0], query[1]) in prerequisites for query in queries]


s = Solution()
print(s.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))
