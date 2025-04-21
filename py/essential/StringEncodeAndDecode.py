# Blind
# Neet
# Grind
# https://neetcode.io/problems/string-encode-and-decode

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # 5#hello
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


s = Solution()
print(s.decode(s.encode(["hello", "#world"])))
