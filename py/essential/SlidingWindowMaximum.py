# https://leetcode.com/problems/sliding-window-maximum/description/
# Monotonic Queue,Sliding Window
# Neet
# Grind

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()  # d[0] is always the largest in the window
        res = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, d = {} and res = {}".format(i, n, d, res))
            while d and nums[d[-1]] < n:
                d.pop()
                print(
                    "\t Popped from d because d has elements and nums[d.top] < curr element"
                )
            d.append(i)
            print("\t Added i to d")
            if d[0] == i - k:
                d.popleft()
                print(
                    "\t Popped left from d because it's outside the window's leftmost (i-k)"
                )
            if i >= k - 1:
                res.append(nums[d[0]])
                print("\t Append nums[d[0]] = {} to res".format(nums[d[0]]))
        return res


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(s.maxSlidingWindow(nums, k))
nums = [5,4,3,2,1]
k = 3
print(s.maxSlidingWindow(nums, k))
