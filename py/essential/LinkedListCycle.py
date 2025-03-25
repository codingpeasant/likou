# Blind
# Grind
# https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=oizxjoit
import sys


from typing import Optional
from list_node import *


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowP, fastP = head, head
        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP:
                return True

        return False


s = Solution()
print(s.hasCycle(getSampleLinkedList()))
