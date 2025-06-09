# https://leetcode.com/problems/boats-to-save-people/description/
# Neet

from typing import List


class Solution:
    def numRescueBoats(
        self, people: List[int], limit: int
    ) -> int:  # greedy, simulation
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if (
                people[i] + people[j] <= limit
            ):  # only need one boat for i and j. Else, j needs a boat
                i += 1  # i is saved
            j -= 1
            boats += 1
        return boats


s = Solution()
people = [3, 2, 2, 1]
limit = 3
print(s.numRescueBoats(people, limit))
