# https://leetcode.com/problems/merge-strings-alternately/description/
# Neet

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1),len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        print(i)
        return "".join(res) + word1[i+1:] + word2[i+1:]
    
s = Solution()
input1 = "abc"
input2 = "pqr"
print(s.mergeAlternately(input1,input2))
input1 = "ab"
input2 = "pqrs"
print(s.mergeAlternately(input1,input2))