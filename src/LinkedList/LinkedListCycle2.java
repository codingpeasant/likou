package LinkedList;

public class LinkedListCycle2 {
//    If there exists a cycle, they will meet each other at a node, say x, and x represents the x-th node in this list. Let’s assume the position of cycle start is at y-th node and the length of cycle is m.
//    About runner, it has already run 2x nodes, which is equal to y + m + (x — y) (length to cycle start + length of cycle + nodes to meet walker). So we have 2x = y + m + (x — y), and it can conduct to x = m.
//    About walker, it needs to walk more m — (x — y) = m — x + y nodes to reach cycle start. As we know in 1 that x is equal to m, walker needs to walk more y nodes to reach the node of cycle start.
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode detectCycle(ListNode head) {
        ListNode ptrSlow, ptrFast, ptrSeek;
        ptrFast = ptrSlow = ptrSeek = head;
        while (ptrSlow != null && ptrFast != null && ptrFast.next != null) {
            ptrFast = ptrFast.next.next;
            ptrSlow = ptrSlow.next;
            if (ptrFast == ptrSlow) {
                while (ptrSeek != ptrSlow) {
                    ptrSeek = ptrSeek.next;
                    ptrSlow = ptrSlow.next;
                }
                return ptrSlow;
            }
        }
        return null;
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
        fifth.next = second;

        System.out.println("Begin of loop at the head: " + detectCycle(first).val);

    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        LinkedListCycle2 l = new LinkedListCycle2();
        l.initialize();
    }
}
