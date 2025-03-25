# https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, finishedVisiting = defaultdict(list), set()

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

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

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        canFinish = len(q)
        while q:
            course = q.popleft()
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    canFinish += 1
        return canFinish == numCourses


s = Solution()
print(s.canFinish1(5, [[3, 0], [3, 2], [1, 3], [1, 4], [4, 3]]))
print(s.canFinish1(2, [[1, 0]]))
print(s.canFinish1(2, [[1, 0], [0, 1]]))
print(s.canFinish1(3, [[1, 0], [1, 2], [0, 1]]))
