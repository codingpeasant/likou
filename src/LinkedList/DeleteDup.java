package LinkedList;

public class DeleteDup {
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
        ListNode ptr = head;
        ListNode ptrNext = head.next;
        while(ptrNext != null) {
            if (ptr.val != ptrNext.val) {
                ptr.next = ptrNext;
                ptr = ptrNext;
            }
            ptrNext = ptrNext.next;
            if (ptrNext == null) {
                ptr.next = null;
            }
        }
        return head;
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

        ListNode newList = deleteDuplicates(first);
        ListNode ptr = newList;
        while(ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        DeleteDup l = new DeleteDup();
        l.initialize();
    }
}
