# https://leetcode.com/problems/satisfiability-of-equality-equations/
# String,Graph,DFS

import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: "List[str]") -> "bool":
        graph = collections.defaultdict(set)  # graph
        notEquals = []

        def can_meet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in graph[u]:
                if not v in visited and can_meet(v, target, visited):
                    return True
            return False

        for eq in equations:  # != means v and u should not be connected in the graph
            if eq[1:3] == "!=":
                a, b = eq.split("!=")
                notEquals.append((a, b))
                continue
            u, v = eq.split("==")
            graph[u].add(v)
            graph[v].add(u)

        for u, v in notEquals:
            if can_meet(u, v, set()):
                return False
        return True


s = Solution()
input = ["a==b", "b==a", "c!=a"]
print(s.equationsPossible(input))
