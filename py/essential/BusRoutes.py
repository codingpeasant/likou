# https://leetcode.com/problems/bus-routes/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a mapping from bus stop to bus routes
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # BFS to find the shortest path
        queue = deque([source])
        visited_stops = {source}
        visited_routes = set()
        buses = 0

        while queue:
            buses += 1
            for _ in range(len(queue)):
                current_stop = queue.popleft()
                for route_index in stop_to_routes[current_stop]:
                    if route_index in visited_routes:
                        continue
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop == target:
                            return buses
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)

        return -1

    # My version
    def numBusesToDestination1(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stopsSet:List[set] = [set(route) for route in routes]

        graph = defaultdict(list)
        for i in range(len(stopsSet)):
            for j in range(i+1, len(stopsSet)):
                if stopsSet[i].intersection(stopsSet[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        res, q = 1, deque([i for i, stops in enumerate(stopsSet) if source in stops])
        visitedBusIds = set()
        while q:
            for _ in range(len(q)):
                busId=q.popleft()
                visitedBusIds.add(busId)
                if target in stopsSet[busId]:
                    return res
                for nei in graph[busId]:
                    if not nei in visitedBusIds:
                        q.append(nei)
            res+=1
        return -1
                    

s=Solution()
print(s.numBusesToDestination1([[1,2,7],[3,6,7]], 1, 6)) # 2
print(s.numBusesToDestination1([[1,2,3],[2,3,4],[4,5,6]], 1, 6))
print(s.numBusesToDestination1([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))