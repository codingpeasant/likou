package LinkedList;

import java.util.HashSet;
import java.util.Set;
// https://leetcode.com/problems/intersection-of-two-linked-lists/
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

    public ListNode getIntersectionNode1(ListNode headA, ListNode headB) {
        Set<ListNode> uniqueValues = new HashSet<>();
        ListNode ptr1 = headA;
        while (ptr1 != null) {
            uniqueValues.add(ptr1);
            ptr1 = ptr1.next;
        }

        ListNode ptr2 = headB;
        while (ptr2 != null) {
            if (!uniqueValues.add(ptr2)) {
                return ptr2;
            }
            ptr2 = ptr2.next;
        }

        return null;
    }
}
