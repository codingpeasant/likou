# https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=rabvlt31
# Grind


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == "]":
                last_str, num = stack.pop()
                current_str = last_str + current_str * num
            else:
                current_str += char

        return current_str


s = Solution()
print(s.decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(s.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
print(s.decodeString("abc3[cd]xyz"))  # Output: "abccdcdcdxyz"
