# https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import Optional

from list_node import *


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        n = count // k  # No. of groups to be reversed
        prev = dummy = ListNode(-1)
        dummy.next = head
        while n:
            curr = prev.next
            next = curr.next
            print(f"prev: {prev.val}; curr: {curr.val}; next: {next.val}")
            for _ in range(
                1, k
            ):  # If we have to reverse k nodes then k-1 links will be reversed
                curr.next = next.next
                next.next = curr
                prev.next = next
                next = curr.next
            prev = curr
            n -= 1
        return dummy.next

    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # begin is the node before the group to be reversed
        # end is the node after the group to be reversed
        def reverse(begin: ListNode, end: ListNode) -> ListNode:
            cur = begin.next
            prev = begin
            first = cur
            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            first.next = cur  # link to the first node in the next group
            begin.next = prev  # link the last node in the previous group to the first node in the current group
            return first

        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                begin = reverse(
                    begin, head.next
                )  # begin is the prev node of the first node in the next group to reverse
                head = begin.next
                print(f"head: {head.val}")
            else:
                head = head.next
        return dummy.next


s = Solution()
printLinkedList(s.reverseKGroup1(getSampleLinkedList(), 2))
# printLinkedList(s.reverseKGroup(getSampleLinkedList(), 3))
