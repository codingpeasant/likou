# https://leetcode.com/problems/network-delay-time/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from collections import defaultdict
import heapq
from typing import List

# Dijkstra's algorithm implementation
# similar with prim's algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for x,y,w in times:
            graph[x].append((w, y))
        
        visited=set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited)==n:
                return travel_time
            
            for time, adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time+time, adjacent_node))

        return -1
  
s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print(s.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))  # 3
print(s.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 4, 1))  # -1