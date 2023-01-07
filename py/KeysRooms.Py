# https://leetcode.com/problems/keys-and-rooms/description/

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room: int) -> bool:
            visited.add(room)
            if len(visited) == n:
                return True
            for keyToRoom in rooms[room]:
                if keyToRoom not in visited:
                    if dfs(keyToRoom):
                        return True
            return False

        return dfs(0)


s = Solution()
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(s.canVisitAllRooms(rooms))
