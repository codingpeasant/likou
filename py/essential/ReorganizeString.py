# https://leetcode.com/problems/reorganize-string/description/
# Neet

import heapq
from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
            
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        res = []
        
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            
            res.extend([char1, char2])
            
            # freq is supposed to be negative so +1 means subtracting 1
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))
                
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1: # Not possible to reorg the string
                return ""
            res.append(char)
            
        return "".join(res)

s=Solution()
print(s.reorganizeString('aab'))