package LinkedList;

public class DeleteDup2 {
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

    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;
        while (curr != null) {
            while (curr.next != null && prev.next.val == curr.next.val) { // TO REACH AT THE END OF DUPLICATES OF CERTAIN VALUE
                curr = curr.next;
            }
            if (prev.next == curr) { // NO DUPLICATES IN BETWEEN CURR AND PREVIOUS
                prev = prev.next;
            } else { // IF THERE IS DUPLICATES, THEN UPDATE PREVIOUS NEXT TO CURRENT NEXT
                prev.next = curr.next;
            }
            curr = curr.next; // UPDATE CURRENT TO CURRENT NEXT
        }
        return dummy.next; // RETURN HEAD
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

        ListNode newList = deleteDuplicates(first);
        ListNode ptr = newList;
        while (ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        DeleteDup2 l = new DeleteDup2();
        l.initialize();
    }
}
