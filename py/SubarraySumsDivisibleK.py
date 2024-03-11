# https://leetcode.com/problems/subarray-sums-divisible-by-k/

import collections
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        ans = 0
        presum = 0
        for num in A:
            presum += num
            ans += dic[
                presum % k
            ]  # Why adding all the prev with the same mod? The new presum could combine with the previous n same mode in (n - 1) ways, plus itself
            # (2 3) (2 3) (1 4): when at 4, mod is 0. Previously there were 3 and (1 4) has 2 ways to combine: (2 3) (1 4) / (2 3) (2 3) (1 4) + (1 4)
            dic[presum % k] += 1
        return ans


s = Solution()
input = [2, 3, 2, 3, 1, 4]
print(s.subarraysDivByK(input, 5))
