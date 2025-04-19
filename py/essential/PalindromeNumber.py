# https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=rabvlt31
# Grind


class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_str = str(x)
        left, right = 0, len(int_str) - 1
        while left <= right:
            if int_str[left] != int_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome1(self, x: int) -> bool:
        int_str = str(x)
        return int_str == int_str[::-1]


s = Solution()
print(s.isPalindrome(121))  # True
print(s.isPalindrome(-121))  # False
