# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
# Neet

from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = dict()
        for u, v, w in edges: 
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))
            
        ref = self.mst(n, graph)
        critical, pseudo = [], []
        for i in range(len(edges)):
            if self.mst(n, graph, exclude=edges[i][:2]) > ref: critical.append(i)
            elif self.mst(n, graph, init=edges[i]) == ref: pseudo.append(i)
        return [critical, pseudo]
            
        
    def mst(self, n, graph, init=None, exclude=None):
        """Return weight of MST of given graph using Prim's algo"""

        def visit(u): 
            """Mark node and put its edges to priority queue"""
            marked[u] = True
            for v, w in graph.get(u, []):
                if exclude and u in exclude and v in exclude: continue
                if not marked[v]: heappush(pq, (w, u, v))
                    
        ans = 0
        marked = [False]*n
        pq = [] #min prioirty queue
        
        if init: 
            u, v, w = init
            ans += w
            marked[u] = marked[v] = True
            visit(u) or visit(v)
        else:
            visit(0)

        while pq: 
            w, u, v = heappop(pq)
            if marked[u] and marked[v]: continue
            ans += w
            if not marked[u]: visit(u)
            if not marked[v]: visit(v)
                
        return ans if all(marked) else inf

s=Solution()
print(s.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))