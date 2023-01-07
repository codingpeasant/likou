# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        result = letters + digits  # put digit logs after letter logs
        return result


s = Solution()
logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "et1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero",
]
print(s.reorderLogFiles(logs=logs))
