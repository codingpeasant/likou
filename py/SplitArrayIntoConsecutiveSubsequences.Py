# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Greedy,Hash Table

from typing import Counter, List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(
            nums
        )  # left[i] counts the number of i that I haven't placed yet.
        end = (
            Counter()
        )  # end is a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
        for num in nums:
            if not left[num]:
                continue
            left[num] -= 1
            if (
                end[num - 1] > 0
            ):  # add a number to the end of a existing consecutive subsequence: The key point of this solution is If there is a valid subsequence ended with x-1, place current x at the end of subsequence always better/less risk than create a new subsequence started with x due to has length at least 3.
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:  # two following number in the left
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True


s = Solution()
nums = [2, 2, 4, 4, 6, 6]
print(s.isPossible(nums))
