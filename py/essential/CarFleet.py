# https://leetcode.com/problems/car-fleet/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        time_to_reach_target = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > time_to_reach_target: # previous car is slower than its next car which was the previous car in the loop. So it cannot catch up and it will be a new fleet
                fleets += 1
                time_to_reach_target = time

        return fleets
  
s=Solution()
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3