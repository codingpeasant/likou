# https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=oizxjoit
# Blind

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, finishedVisiting = defaultdict(list), set()

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        def hasLoop(node: int, visited: set) -> bool:
            if (
                node in finishedVisiting
            ):  # memory to avoid multiple dfs on a single node
                return
            if node in visited:
                return True  # cycle found
            visited.add(node)
            for nei in graph[node]:
                if hasLoop(nei, visited):
                    return True
            visited.remove(node)
            finishedVisiting.add(node)

            return False

        for node in range(numCourses):
            if hasLoop(node, set()):
                return False
        return True


s = Solution()
print(s.canFinish(5, [[3, 0], [3, 2], [1, 3], [1, 4], [4, 3]]))
