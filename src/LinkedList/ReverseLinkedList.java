package LinkedList;

public class ReverseLinkedList {
    class ListNode {
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

    public ListNode reverseList(ListNode head) {
        /* iterative solution */
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }

    public void initialize() {
        ListNode first = new ListNode(2);
        ListNode second = new ListNode(5);
        ListNode third = new ListNode(1);
        ListNode fourth = new ListNode(1);
        ListNode fifth = new ListNode(3);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;

        ListNode newList = reverseList(first);
        ListNode ptr = newList;
        while (ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        ReverseLinkedList l = new ReverseLinkedList();
        l.initialize();
    }
}
