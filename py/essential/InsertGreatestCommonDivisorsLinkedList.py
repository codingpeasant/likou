from math import gcd
from typing import Optional
from list_node import *


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head

        while curr is not None and curr.next is not None:
            curr.next = ListNode(gcd(curr.val, curr.next.val), next=curr.next)
            curr = curr.next.next

        return head


s = Solution()
printLinkedList(s.insertGreatestCommonDivisors(getSampleLinkedList()))
