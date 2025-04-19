# https://leetcode.com/problems/course-schedule-ii/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet
# Grind

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []  # almost the same with CourseSchedule
        while q:
            course = q.popleft()
            res.append(course)
            if len(res) == numCourses:
                return res
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return []


s = Solution()
print(s.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
print(s.findOrder(2, [[1, 0]]))
print(s.findOrder(2, [[1, 0], [0, 1]]))
print(s.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
