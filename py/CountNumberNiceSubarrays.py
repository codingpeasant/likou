# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

from typing import List


# Just keep count of the current odd number.
# Look in the dictionary if we can find (currendOds - k),
# if it exists that means I can get an subarray with k odds.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = {0: 1} # key: 
        cnt = res = 0
        for num in nums:
            if num % 2 == 1:
                cnt += 1

            if cnt - k in dic:
                res += dic[cnt - k]

            dic[cnt] = dic.get(cnt, 0) + 1
        return res

s = Solution()
nums = [2, 2, 2, 1, 2, 2, 1, 2, 1, 2]
k = 2
print(s.numberOfSubarrays(nums, k))
