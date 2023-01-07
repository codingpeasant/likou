# https://leetcode.com/problems/check-if-the-sentence-is-pangram/


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_set = set()
        for letter in sentence:
            letter_set.add(letter)
        return len(letter_set) == 26


s = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))
