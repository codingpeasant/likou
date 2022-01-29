package Concurrency;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.ca/2019-03-02-1188-Design-Bounded-Blocking-Queue/
public class DesignBoundedBlockingQueue {
    int size;
    final Queue<Integer> queue;

    public DesignBoundedBlockingQueue(int capacity) {
        this.queue = new LinkedList<>();
        this.size = capacity;
    }

    public void enqueue(int element) throws InterruptedException {
        synchronized (queue) {
            while (queue.size() == size) {
                queue.wait();
            }
            queue.offer(element);
            queue.notifyAll();
        }
    }

    public int dequeue() throws InterruptedException {
        synchronized (queue) {
            while (queue.size() == 0) {
                queue.wait();
            }
            int num = queue.poll();
            queue.notifyAll();
            return num;
        }
    }

    public int size() {
        synchronized (queue) {
            return queue.size();
        }
    }
}
