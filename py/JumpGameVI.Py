# https://leetcode.com/problems/jump-game-vi/

from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque(
            [0]
        )  # store index of `nums` elements, elements is in decreasing order, the front is the maximum element.
        for i in range(1, n):
            # nums[i] = max(nums[i-k], nums[i-k+1],.., nums[i-1]) + nums[i] = nums[dq.front()] + nums[i]
            nums[i] = nums[dq[0]] + nums[i]

            # Add a nums[i] to the deq
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()  # Eliminate elements less or equal to nums[i], which will never be chosen in the future
            dq.append(i)

            # Remove if the last element is out of window size k
            if i - dq[0] >= k:
                dq.popleft()

        return nums[n - 1]
    
    def maxResult1(self, nums: List[int], k: int) -> int: # same with above but use a dp array
        max_score_at, n = [-float("inf")] * len(nums), len(nums)
        max_score_at[0] = nums[0]
        dq = deque([0])
        for i in range(1, n):
            max_score_at[i] = nums[dq[0]] + nums[i]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i - dq[0] >=k:
                dq.popleft()
        return max_score_at[n-1]


s = Solution()
print(s.maxResult([1, -1, -2, 4, -7, 3], 2))
print(s.maxResult1([1, -1, -2, 4, -7, 3], 2))
