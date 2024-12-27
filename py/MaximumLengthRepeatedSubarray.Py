# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max(max(row) for row in dp)


s = Solution()
nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7, 6, 8]
# nums1 = [0, 0, 0, 0, 0]
# nums2 = [0, 0, 0, 0, 0]
print(s.findLength(nums1, nums2))
