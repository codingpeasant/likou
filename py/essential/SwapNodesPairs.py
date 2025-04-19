# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Linked List
# Grind

from typing import Optional
from list_node import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next # next pair node = 3 
            second = cur.next # 2

            second.next = cur # 2 -> 1
            cur.next = npn # 1 -> 3
            prev.next = second # dummy -> 2

            prev = cur # prev = 1
            cur = npn # cur = 3
        
        return dummy.next


s = Solution()
input = getSampleLinkedList()
printLinkedList(s.swapPairs(input))
