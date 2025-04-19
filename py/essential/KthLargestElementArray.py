# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=plakya4j
# Neet
# Grind

import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # not stable: can be N^2 if the pivot is always the largest or smallest element
        # in the array. But on average, it is O(N)
        def partition(l, r, pivot):
            pivot_elem = nums[pivot]  # Store Pivot Element:
            nums[r], nums[pivot] = (
                nums[pivot],
                nums[r],
            )  # Move Pivot to the End to temporarily move it out of the way.

            index = l
            for i in range(l, r):
                if nums[i] < pivot_elem:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1

            # Move Pivot to Its Final Position. nums[r] is the Pivot Element
            nums[index], nums[r] = nums[r], nums[index]
            return index

        def quick_select(l, r, kth_index):
            if l == r:
                return nums[l]

            # simply pick the first element as the pivot; could be random.randint(l, r)
            pivot_index = partition(l, r, random.randint(l, r))

            if pivot_index == kth_index:
                return nums[pivot_index]

            if kth_index > pivot_index:
                return quick_select(pivot_index + 1, r, kth_index)
            else:
                return quick_select(l, pivot_index - 1, kth_index)

        return quick_select(0, n - 1, n - k)

    # nlogk
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None

        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, num)
        return minheap[0]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print(s.findKthLargest([1, 1, 1, 1, 1, 1], 4))  # 1
print(s.findKthLargest1([3, 2, 1, 5, 6, 4], 2))  # 5
print(s.findKthLargest1([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print(s.findKthLargest1([1, 1, 1, 1, 1, 1], 4))  # 1
