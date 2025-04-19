# https://leetcode.com/problems/partition-labels/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastCharToIndex = defaultdict(int)
        for i, letter in enumerate(s):
            lastCharToIndex[letter] = i
        partitions = []
        start = 0
        maxIndexForAllTheCharsFromStart = 0
        for i, letter in enumerate(s):
            # greedy
            maxIndexForAllTheCharsFromStart = max(maxIndexForAllTheCharsFromStart, lastCharToIndex[letter])
            if i == maxIndexForAllTheCharsFromStart:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]
print(s.partitionLabels("eccbbbbdec"))  # [10]