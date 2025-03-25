# https://leetcode.com/problems/first-bad-version/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def isBadVersion(version: int) -> bool:
        if version > 3:
            return True
        else:
            return False

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if Solution.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.firstBadVersion(9))
