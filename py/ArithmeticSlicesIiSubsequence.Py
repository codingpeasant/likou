# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A):
        total, n = 0, len(A)
        dp = [
            defaultdict(int) for _ in A
        ]  # dp[i][d] denotes the number of arithmetic subsequences that ends with A[i] and its common difference is d.
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][
                    diff
                ]  # only collect until the previous because the counter is added by 1 when there were 2 elements like dp[1][2] = 1 and we need at least 3 elements
        return total


s = Solution()
input = [2, 4, 6, 8]
print(s.numberOfArithmeticSlices(input))
