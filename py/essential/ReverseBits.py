# https://leetcode.com/problems/reverse-bits/description/?envType=problem-list-v2&envId=oizxjoit
# Blind


class Solution:
    def reverseBits(
        self, n
    ):  # reverse is for index position 1 <-> 32, 2 <-> 31, 3 <-> 30....
        res = 0
        for i in range(32):  # for all the bits
            if n & 1:  # last bit is 1
                res += 1 << (31 - i)  # add it to the front
            n >>= 1  # remove last bit
        return res


s = Solution()
print(s.reverseBits(1))
