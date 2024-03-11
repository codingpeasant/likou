# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        jmin = jmax = jbad = -1
        for i, a in enumerate(nums):
            if not minK <= a <= maxK:
                jbad = i
            if a == minK:
                jmin = i
            if a == maxK:
                jmax = i
            res += max(
                0, min(jmin, jmax) - jbad
            )  # basic rule for subarray problems: the number of subarray increases by i when the array grows from i-1 elements to i elements
        return res


s = Solution()
print(s.countSubarrays([1, 5, 3, 1], 1, 5))
