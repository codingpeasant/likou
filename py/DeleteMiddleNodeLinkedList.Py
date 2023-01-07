# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

import math
from typing import Optional
from list_node import *


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(-math.inf)
        dummy.next = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next


s = Solution()
input = getSampleLinkedList()
output = s.deleteMiddle(input)
printLinkedList(output)
