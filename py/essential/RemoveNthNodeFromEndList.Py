# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Linked List,Two Pointers
# Blind
# Neet

from typing import Optional
from list_node import *


# destination is the (m-n)th node, fast moved n times and there is (m-n) times to move to the end
# so slow moves (m-n) times to reach (m-n)th node when fast is at the end
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # advance fast to nth position
        for _ in range(n):
            fast = fast.next

        if not fast:  # to remove the first node
            return head.next

        # then advance both fast and slow now they are nth positions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


s = Solution()
input = getSampleLinkedList()
head = s.removeNthFromEnd(input, 2)
printLinkedList(head)
