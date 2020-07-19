package LinkedList;

import java.util.HashSet;
import java.util.Set;

public class IntersectionTwoLinkedLists {
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> uniqueValues = new HashSet<>();
        ListNode ptr = headA;
        while (ptr != null) {
            uniqueValues.add(ptr);
            ptr = ptr.next;
        }

        ptr = headB;
        while (ptr != null) {
            if (uniqueValues.contains(ptr)) {
                return ptr;
            }
            ptr = ptr.next;
        }

        return null;
    }
}
