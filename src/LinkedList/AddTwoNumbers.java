package LinkedList;

import org.w3c.dom.NodeList;

public class AddTwoNumbers {
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

    public ListNode addTwoNumbers(ListNode first, ListNode second) {
        ListNode res = null; // res is head node of the resultant list
        ListNode prev = null;
        ListNode temp = null;
        int carry = 0, sum;

        while (first != null || second != null) //while both lists exist
        {
            // Calculate value of next digit in resultant list.
            // The next digit is sum of following things
            // (i)  Carry
            // (ii) Next digit of first list (if there is a next digit)
            // (ii) Next digit of second list (if there is a next digit)
            sum = carry + (first != null ? first.val : 0) + (second != null ? second.val : 0);

            // update carry for next calulation
            carry = (sum >= 10) ? 1 : 0;

            // update sum if it is greater than 10
            sum = sum % 10;

            // Create a new node with sum as data
            temp = new ListNode(sum);

            // if this is the first node then set it as head of
            // the resultant list
            if (res == null) {
                res = temp;
            } else // If this is not the first node then connect it to the rest.
            {
                prev.next = temp;
            }

            // Set prev for next insertion
            prev = temp;

            // Move first and second pointers to next nodes
            if (first != null) {
                first = first.next;
            }
            if (second != null) {
                second = second.next;
            }
        }

        if (carry > 0) {
            temp.next = new ListNode(carry);
        }

        // return head of the resultant list
        return res;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(9);
        ListNode third = new ListNode(9);
        ListNode fourth = new ListNode(9);
        ListNode fifth = new ListNode(9);
        ListNode fifth1 = new ListNode(9);
        ListNode fifth2 = new ListNode(9);
        ListNode fifth3 = new ListNode(9);
        ListNode fifth4 = new ListNode(9);
        ListNode fifth5 = new ListNode(9);


        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;
        fifth.next = fifth1;
        fifth1.next = fifth2;
        fifth2.next = fifth3;
        fifth3.next = fifth4;
        fifth4.next = fifth5;

        ListNode first2 = new ListNode(9);

        ListNode newList = addTwoNumbers(first, first2);
        ListNode ptr = newList;
        while (ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        AddTwoNumbers a = new AddTwoNumbers();
        a.initialize();
    }
}
