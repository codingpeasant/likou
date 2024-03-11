# https://leetcode.com/problems/string-compression/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        index, indexAns = 0, 0
        while index < len(chars):
            count, curChar = 0, chars[index]
            while index < len(chars) and chars[index] == curChar:
                count += 1
                index += 1
            chars[indexAns] = curChar
            indexAns += 1

            if count > 1:
                for c in str(count):
                    chars[indexAns] = c
                    indexAns += 1
        return indexAns


s = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(s.compress(chars))
