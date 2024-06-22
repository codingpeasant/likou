# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
# Stack,Cache


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [c, count]
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join(char * k for char, k in stack)


s = Solution()
print(s.removeDuplicates("pbbcggttciiippooaais", 2))
