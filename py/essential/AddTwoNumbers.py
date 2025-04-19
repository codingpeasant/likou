# https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet
# Grind

from typing import Optional

from list_node import *


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


s = Solution()
printLinkedList(
    s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), getSampleLinkedList())
)
print(s.addTwoNumbers(ListNode(0), ListNode(0)))  # 0
