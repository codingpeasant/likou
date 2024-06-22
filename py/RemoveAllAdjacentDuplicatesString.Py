# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Stack


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)


s = Solution()
print(s.removeDuplicates("abbaca"))
