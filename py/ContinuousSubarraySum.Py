# https://leetcode.com/problems/continuous-subarray-sum/

from typing import List


class Solution:

    # (presum[i] - presum[j]) % k = 0 ==> presum[i] % k = presum[j] % k
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_index_dict = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            mod = sum % k
            if mod in mod_index_dict:
                if i > 0 and i - mod_index_dict[mod] >= 2:
                    return True
            else:  # only keep the first occurrence of sum % k
                mod_index_dict[mod] = i

        return False


s = Solution()
nums = [1, 2, 3]
k = 5
print(s.checkSubarraySum(nums, k))
