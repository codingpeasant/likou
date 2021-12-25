package LinkedList;

// https://leetcode.com/problems/middle-of-the-linked-list/
public class MiddleLinkedList {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(1);
        ListNode third = new ListNode(1);
        ListNode fourth = new ListNode(1);
        ListNode fifth = new ListNode(2);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;

        ListNode midNode = middleNode(first);
        System.out.println(midNode.val);
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        MiddleLinkedList l = new MiddleLinkedList();
        l.initialize();
    }
}
