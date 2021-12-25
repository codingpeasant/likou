package LinkedList;

// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
public class RemoveNthNode {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        ListNode slow = dummy, fast = dummy;
        dummy.next = head;

        //Move fast in front so that the gap between slow and fast becomes n
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        //Move fast to the end, maintaining the gap; move n + 1 times
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        //Skip the desired node
        slow.next = slow.next.next;
        return dummy.next;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(2);
        ListNode third = new ListNode(3);
        ListNode fourth = new ListNode(4);
        ListNode fifth = new ListNode(5);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;

        ListNode newList = removeNthFromEnd(first, 5);
        ListNode ptr = newList;
        while (ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        RemoveNthNode l = new RemoveNthNode();
        l.initialize();
    }
}
