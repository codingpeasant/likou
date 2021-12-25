package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/reverse-linked-list/
public class ReverseLinkedList {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }

        ListNode() {
        }

        ListNode(int x, ListNode next) {
            val = x;
            this.next = next;
        }
    }

    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        Stack<ListNode> stack = new Stack<>();
        ListNode ptr = head;
        ListNode ptrNew = new ListNode();
        while (ptr != null) {
            stack.push(ptr);
            ptr = ptr.next;
        }

        ListNode temp = null;
        while (!stack.isEmpty()) {
            ListNode cur = stack.pop();
            if (cur.next == null) {
                ptrNew = cur;
            } else {
                temp.next = cur;
            }
            temp = cur;
        }
        temp.next = null;

        return ptrNew;
    }

    // no extra space
    public ListNode reverseList2(ListNode head) {
        ListNode dummy = new ListNode(0);

        while (head != null) {
            ListNode temp = head;
            head = head.next;
            temp.next = dummy.next;
            dummy.next = temp;
        }
        return dummy.next;
    }

    public ListNode reverseList3(ListNode head) {
        if (head.next == null) return head;
        ListNode last = reverseList3(head.next);
        head.next.next = head;
        head.next = null;
        return last;
    }

    public void initialize() {
        ListNode first = new ListNode(5);
        ListNode second = new ListNode(9);
        ListNode third = new ListNode(3);
        ListNode fourth = new ListNode(1);
        ListNode fifth = new ListNode(2);

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
        System.out.print("\n");

        ListNode first2 = new ListNode(5);
        ListNode second2 = new ListNode(9);
        ListNode third2 = new ListNode(3);
        ListNode fourth2 = new ListNode(1);
        ListNode fifth2 = new ListNode(2);

        first2.next = second2;
        second2.next = third2;
        third2.next = fourth2;
        fourth2.next = fifth2;


        ListNode newList2 = reverseList2(first2);
        ListNode ptr2 = newList2;
        while (ptr2 != null) {
            System.out.print(ptr2.val + " -> ");
            ptr2 = ptr2.next;
        }

        System.out.print("\n");

        ListNode first3 = new ListNode(5);
        ListNode second3 = new ListNode(9);
        ListNode third3 = new ListNode(3);
        ListNode fourth3 = new ListNode(1);
        ListNode fifth3 = new ListNode(2);

        first3.next = second3;
        second3.next = third3;
        third3.next = fourth3;
        fourth3.next = fifth3;


        ListNode newList3 = reverseList3(first3);
        ListNode ptr3 = newList3;
        while (ptr3 != null) {
            System.out.print(ptr3.val + " -> ");
            ptr3 = ptr3.next;
        }
    }


    public static void main(String[] args) {
        ReverseLinkedList r = new ReverseLinkedList();
        r.initialize();
    }
}
