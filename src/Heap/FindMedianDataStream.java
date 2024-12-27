package Heap;

import java.util.PriorityQueue;
import java.util.Queue;

// https://leetcode.com/problems/find-median-from-data-stream/
public class FindMedianDataStream {
    private final Queue<Integer> largerHalf = new PriorityQueue<>(); // min heap
    private final Queue<Integer> smallerHalf = new PriorityQueue<>((a, b) -> b - a); // max heap
    private boolean even = true;

    public FindMedianDataStream() {

    }

    public double findMedian() {
        if (even)
            return (smallerHalf.peek() + largerHalf.peek()) / 2.0;
        else
            return smallerHalf.peek();
    }

    public void addNum(int num) { // smaller half is equal or larger by 1
        if (even) {
            largerHalf.offer(num);
            smallerHalf.offer(largerHalf.poll());
        } else {
            smallerHalf.offer(num);
            largerHalf.offer(smallerHalf.poll());
        }
        even = !even;
    }

    public static void main(String[] args) {
        FindMedianDataStream f = new FindMedianDataStream();
        f.addNum(1);
        f.addNum(2);
        f.addNum(3);
        f.addNum(4);
        System.out.println(f.findMedian());
        f.addNum(5);

        System.out.println(f.findMedian());
    }
}
