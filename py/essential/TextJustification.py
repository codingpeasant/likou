# https://leetcode.com/problems/text-justification/description/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                    print(cur)
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [" ".join(cur).ljust(maxWidth)]


s = Solution()
print(
    s.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
)
