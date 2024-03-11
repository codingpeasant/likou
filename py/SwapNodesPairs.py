# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import Optional
from list_node import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            temp = current.next
            temp2 = current.next.next.next

            current.next = current.next.next
            current.next.next = temp
            current.next.next.next = temp2

            current = current.next.next
        return dummy.next


s = Solution()
input = getSampleLinkedList()
print(s.swapPairs(input).val)
