# https://leetcode.com/problems/maximum-units-on-a-truck/


from typing import List, Tuple

# greedy
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0

        for box_type in boxTypes:
            if truckSize < 1:
                break
            minSize = min(truckSize, box_type[0])
            truckSize -= minSize
            res += minSize * box_type[1]
        return res


s = Solution()

input = [[5, 10], [2, 5], [4, 7], [3, 9]]
print(s.maximumUnits(input, 10))
