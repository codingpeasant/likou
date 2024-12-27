# Blind
# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=oizxjoit

from typing import Optional

from list_node import *


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = head = ListNode()
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        head.next = head1 if head1 else head2

        return res.next


s = Solution()
printLinkedList(s.mergeTwoLists(getSampleLinkedList(), getSampleLinkedList()))
