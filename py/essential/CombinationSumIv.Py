# https://leetcode.com/problems/combination-sum-iv/
# Grind
# Neet


# similar with coin-change-ii but allows different order (1,3) and (3,1) are different
# comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1]
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
