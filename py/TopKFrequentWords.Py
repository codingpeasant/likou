# https://leetcode.com/problems/top-k-frequent-words/
# Heap

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        words_heap = [(-word_counts[word], word) for word in word_counts]
        heapq.heapify(words_heap)
        return [heapq.heappop(words_heap)[1] for _ in range(k)]


s = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(s.topKFrequent(words, k))
