package LinkedList;

// https://leetcode.com/problems/merge-two-sorted-lists/
public class MergeTwoSortedLists {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode p3 = dummy;

        while (p1 != null && p2 != null) {
            if (p1.val <= p2.val) {
                p3.next = new ListNode(p1.val);
                p1 = p1.next;
            } else {
                p3.next = new ListNode(p2.val);
                p2 = p2.next;
            }
            p3 = p3.next;
        }

        while (p1 != null) {
            p3.next = new ListNode(p1.val);
            p3 = p3.next;
            p1 = p1.next;
        }

        while (p2 != null) {
            p3.next = new ListNode(p2.val);
            p3 = p3.next;
            p2 = p2.next;
        }

        return dummy.next;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(2);
        ListNode third = new ListNode(4);
        ListNode fourth = new ListNode(1);
        ListNode fifth = new ListNode(3);
        ListNode sixth = new ListNode(4);

        first.next = second;
        second.next = third;

        fourth.next = fifth;
        fifth.next = sixth;

        ListNode ptr = mergeTwoLists(first, fourth);
        while(ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        MergeTwoSortedLists l = new MergeTwoSortedLists();
        l.initialize();
    }
}
