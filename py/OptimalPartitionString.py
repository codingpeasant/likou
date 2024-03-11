# https://leetcode.com/problems/optimal-partition-of-string/


class Solution:
    def partitionString(self, s: str) -> int:
        if not s:
            return 0
        res, hashset = 0, set()
        for letter in s:
            if letter in hashset:
                res += 1
                hashset.clear()
            hashset.add(letter)
        return res + 1


s = Solution()
input = "abacaba"
print(s.partitionString(input))
