# https://leetcode.com/problems/reverse-linked-list-ii/
# https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)

from multiprocessing import dummy
from typing import Optional

from list_node import ListNode


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head
        p = dummy = ListNode(None)
        dummy.next = head
        for _ in range(left - 1):
            p = p.next
        tail = p.next
        for _ in range(right - left):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
res: ListNode = s.reverseBetween(node1, 2, 4)
while res:
    print(res.val)
    res = res.next
