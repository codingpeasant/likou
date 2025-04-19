# https://leetcode.com/problems/reconstruct-itinerary/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort() # prioritize lexicographically smaller tickets
        for src, dst in tickets:
            graph[src].append(dst)
        res = ["JFK"]

        # TLE but easier to understand
        def dfs(cur: str):
            if len(res) == len(tickets) + 1: # all the tickets are used
                return True
            if cur not in graph: # dead end but not all tickets are used - doesn't exist in the current setting (all tickets form at least one valid itinerary) but good to check the edge case
                return False
            for i in range(len(graph[cur])): # the for loop with limited iterations to avoid infinite recursion on the same node again
                next = graph[cur].pop(0) # try to remove the first destination to make sure it's only used once
                res.append(next) # try to add it
                if dfs(next):
                    return True
                res.pop() # this path didn't work, so remove the last destination
                graph[cur].append(next) # add it back to the graph
            return False # no path worked
        
        dfs("JFK")
        return res
    
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
        
        dfs("JFK")
        
        return itinerary[::-1]

s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(s.findItinerary(tickets))
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s.findItinerary(tickets))
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]
print(s.findItinerary1(tickets))