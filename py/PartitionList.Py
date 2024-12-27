# https://leetcode.com/problems/partition-list/


from typing import Optional
from list_node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 2 dummy nodes: one points to the smaller elements; another larger ones
        p1 = d1 = ListNode()
        p2 = d2 = ListNode()

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        p1.next = d2.next  # connect the smaller part with larger part
        p2.next = None
        return d1.next


s = Solution()
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

res: ListNode = s.partition(node1, 3)
while res:
    print(res.val)
    res = res.next
