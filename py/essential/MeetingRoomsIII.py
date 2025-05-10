# https://leetcode.com/problems/meeting-rooms-iii/
# Neet

import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings by start time, then end time
        booked = [0] * n  # Count of meetings booked per room
        free_rooms = list(range(n))  # Min-heap of free room indices
        heapq.heapify(free_rooms)
        ongoing_meetings = []  # Min-heap of (end_time, room)

        for start, end in meetings:
            # Free up rooms that have finished their meetings
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Assign a free room
                room = heapq.heappop(free_rooms)
                booked[room] += 1
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # No free rooms, extend the meeting in the earliest available room
                end_time, room = heapq.heappop(ongoing_meetings)
                booked[room] += 1
                heapq.heappush(ongoing_meetings, (end_time + (end - start), room))

        return booked.index(max(booked))
    
s = Solution()
print(s.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])) # 0
print(s.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])) # 1
