# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)
        for path in paths:
            parts = path.split()
            for i in range(1, len(parts)):
                name, content = parts[i].split("(")
                content_to_path[content[:-1]].append(parts[0] + "/" + name)

        return [value for value in content_to_path.values() if len(value) > 1]


s = Solution()
paths = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
]
print(s.findDuplicate(paths))
