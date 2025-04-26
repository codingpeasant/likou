# https://leetcode.com/problems/simplify-path/
# Neet


class Solution:
    def simplifyPath(self, path: str):
        stack = []
        for ele in path.split("/"):
            if ele in ["", "."]:
                continue
            if stack and ele == "..":
                stack.pop()
            elif ele != "..":
                stack.append(ele)
        return "/" + "/".join(stack)


s = Solution()
print(s.simplifyPath('/home/user/Documents/../Pictures'))
print(s.simplifyPath('/../'))
print(s.simplifyPath('/.../a/../b/c/../d/./'))