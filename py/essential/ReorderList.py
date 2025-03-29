# Blind
# Neet
# https://leetcode.com/problems/reorder-list/description/?envType=problem-list-v2&envId=oizxjoit

from typing import Optional
from list_node import *


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: find middle
        if not head:
            return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        slow.next = None
        printLinkedList(head)

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
        printLinkedList(head)
    
    def reorderList1(self, head: Optional[ListNode]) -> None:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        n = len(arr)
        left,right = 0, n - 1
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                break
            arr[right].next = arr[left]
            right -= 1
        arr[left].next = None # or arr[right].next = None
        printLinkedList(arr[0])


s = Solution()
s.reorderList(getSampleLinkedList())
s.reorderList1(getSampleLinkedList())
