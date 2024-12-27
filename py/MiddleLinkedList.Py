# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from list_node import *


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


s = Solution()
input = getSampleLinkedList()
print(s.middleNode(input).val)
