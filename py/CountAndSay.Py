# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n - 1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index - 1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = "".join(temp)
        return s


s = Solution()
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
