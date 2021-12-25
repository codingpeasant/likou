package LinkedList;

import java.util.List;

// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
public class RemoveDuplicatesSortedList {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null) {
            int cur = fast.val;
            while (fast != null && cur == fast.val) {
                cur = fast.val;
                fast = fast.next;
            }
            slow.next = fast;
            slow = fast;
        }

        return head;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(2);
        ListNode third = new ListNode(2);
        ListNode fourth = new ListNode(4);
        ListNode fifth = new ListNode(4);
        ListNode sixth = new ListNode(5);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;
        fifth.next = sixth;

        ListNode newList = deleteDuplicates(first);
        ListNode ptr = newList;
        while (ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    public static void main(String[] args) {
        RemoveDuplicatesSortedList r = new RemoveDuplicatesSortedList();
        r.initialize();
    }
}
