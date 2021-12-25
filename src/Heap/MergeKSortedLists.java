package Heap;

import java.util.PriorityQueue;
import java.util.Queue;
// https://leetcode.com/problems/merge-k-sorted-lists/
public class MergeKSortedLists {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        Queue<Integer> minHeap = new PriorityQueue<>();

        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        for (ListNode linkedList: lists) {
            ListNode ptr = linkedList;
            while (ptr != null) {
                minHeap.add(ptr.val);
                ptr = ptr.next;
            }
        }

        while (!minHeap.isEmpty()) {
            dummy.next = new ListNode(minHeap.poll());
            dummy = dummy.next;
        }
        return head.next;
    }

    public void initialize() {
        ListNode first = new ListNode(1);
        ListNode second = new ListNode(4);
        ListNode third = new ListNode(5);

        ListNode fourth = new ListNode(1);
        ListNode fifth = new ListNode(3);
        ListNode sixth = new ListNode(4);

        ListNode seventh = new ListNode(2);
        ListNode eighth = new ListNode(6);

        first.next = second;
        second.next = third;

        fourth.next = fifth;
        fifth.next = sixth;

        seventh.next = eighth;

        ListNode[] input = new ListNode[3];
        input[0] = first;
        input[1] = fourth;
        input[2] = seventh;

        ListNode ptr = mergeKLists(input);

        while(ptr != null) {
            System.out.print(ptr.val + " -> ");
            ptr = ptr.next;
        }
    }

    public static void main(String[] args) {
        MergeKSortedLists mdt = new MergeKSortedLists();
        mdt.initialize();
    }
}
