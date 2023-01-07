# https://leetcode.com/problems/sum-of-subarray-minimums/

from typing import List

#    I guess this is a general intuition for most solution.
#    res = sum(A[i] * f(i))
#    where f(i) is the number of subarrays,
#    in which A[i] is the minimum.

#    To get f(i), we need to find out:
#    left[i], the length of strict bigger numbers on the left of A[i],
#    right[i], the length of bigger numbers on the right of A[i].

#    Then,
#    left[i] + 1 equals to
#    the number of subarray ending with A[i],
#    and A[i] is single minimum.

#    right[i] + 1 equals to
#    the number of subarray starting with A[i],
#    and A[i] is the first minimum.

#    Finally f(i) = (left[i] + 1) * (right[i] + 1)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        mod = 1000000007
        n = len(arr)
        leftBigger, rightBigger = [0] * n, [0] * n
        s1, s2 = [], []

        for i in range(n):
            count = 1  # add itself
            while s1 and s1[-1][0] > arr[i]:
                count += s1.pop()[1]
            s1.append([arr[i], count])
            leftBigger[i] = count

        for i in reversed(range(n)):
            count = 1
            while s2 and s2[-1][0] >= arr[i]:
                count += s2.pop()[1]
            s2.append([arr[i], count])
            rightBigger[i] = count

        for i in range(n):
            res += arr[i] * leftBigger[i] * rightBigger[i]
            res % mod
        return res


s = Solution()
input = [1, 1, 1]
print(s.sumSubarrayMins(input))
