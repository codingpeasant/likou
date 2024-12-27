package LinkedList;

// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
public class RemoveDuplicatesSortedList2 {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        ListNode current = head;

        while (current != null) {
            boolean dup = false;

            // probe next to see if duplicate
            while (current.next != null && current.val == current.next.val) {
                current = current.next;
                dup = true;
            }

            if (dup) { // prev staying the same
                prev.next = current.next;
            } else {
                prev = current;
            }
            current = current.next;
        }

        return dummy.next;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(1);
        ListNode third = new ListNode(1);
        ListNode fourth = new ListNode(5);
        ListNode fifth = new ListNode(6);
        ListNode sixth = new ListNode(6);

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
        RemoveDuplicatesSortedList2 r = new RemoveDuplicatesSortedList2();
        r.initialize();
    }
}
