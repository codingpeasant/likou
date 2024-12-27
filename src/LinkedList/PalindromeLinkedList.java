package LinkedList;

import java.util.Stack;

// https://leetcode.com/problems/palindrome-linked-list/
public class PalindromeLinkedList {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    // alternative: reverse the second half of the linked list and compare with the first half
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack = new Stack<>();
        ListNode p = head;
        while (p != null) {
            stack.push(p.val);
            p = p.next;
        }
        p = head;
        while (p != null) {
            int value = stack.pop();
            if (value != p.val) {
                return false;
            }
            p = p.next;
        }

        return true;
    }

    public void initialize() {
        ListNode first = new ListNode(5);
        ListNode second = new ListNode(9);
        ListNode third = new ListNode(3);
        ListNode fourth = new ListNode(9);
        ListNode fifth = new ListNode(5);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = fifth;
        System.out.println(isPalindrome(first));
    }

    public static void main(String[] args) {
        PalindromeLinkedList r = new PalindromeLinkedList();
        r.initialize();
    }
}
