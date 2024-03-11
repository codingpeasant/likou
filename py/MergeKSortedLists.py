# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import List, Optional
from list_node import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap, head = [], ListNode(0)
        dummy = head

        for list in lists:
            pointer = list
            while pointer:
                heapq.heappush(minHeap, pointer.val)
                pointer = pointer.next
        while minHeap:
            head.next = ListNode(heapq.heappop(minHeap))
            head = head.next
        return dummy.next


s = Solution()
input = getSampleLinkedList()
head = s.mergeKLists([input])
while head:
    print(head.val)
    head = head.next
