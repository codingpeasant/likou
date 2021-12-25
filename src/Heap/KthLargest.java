package Heap;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

// https://leetcode.com/problems/kth-largest-element-in-a-stream/
public class KthLargest {
    private Queue<Integer> pq = new PriorityQueue<>(); // min heap
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int i: nums) {
            addToQ(i);
        }
    }

    public int add(int val) {
        addToQ(val);
        return pq.peek();
    }

    public void addToQ(int num) {
        pq.add(num);
        if (pq.size() > k) {
            pq.poll(); // remove the smallest
        }
    }

    public static void main(String[] args) {
        int k = 3;
        int[] arr = {4,5,8,2};
        KthLargest kthLargest = new KthLargest(3, arr);

        System.out.println(kthLargest.add(3));   // returns 4
        System.out.println(kthLargest.add(5));   // returns 5
        System.out.println(kthLargest.add(10));  // returns 5
        System.out.println(kthLargest.add(9));   // returns 8
        System.out.println(kthLargest.add(4));   // returns 8

        Queue<Integer> maxHeap = new PriorityQueue<>(
                new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        return - Integer.compare(o1, o2);
                    }
                }
        );
    }
}
