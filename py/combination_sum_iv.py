# https://leetcode.com/problems/combination-sum-iv/

from curses.ascii import SO

# similar with flipper coin
class Solution:
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [0] * (target + 1)
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1
                if num < i:
                    combs[i] += combs[i - num]
        return combs[target]


s = Solution()
nums = [1, 2, 3]
print(s.combinationSum4(nums, 4))
