package Heap;

import java.util.PriorityQueue;

// https://leetcode.com/problems/max-value-of-equation/
//  Because xi < xj,
//  yi + yj + |xi - xj| = (yi - xi) + (xj + yj)
//
//  So for each pair of (xj, yj),
//  we have xj + yj, and we only need to find out the maximum yi - xi
public class MaxValueEquation {
    class Pair<T, Y> {
        T key;
        Y value;

        Pair(T key, Y value) {
            this.key = key;
            this.value = value;
        }

        T getKey() {
            return key;
        }

        Y getValue() {
            return value;
        }
    }

    public int findMaxValueOfEquation(int[][] points, int k) {
        // max heap for key, min heap for value
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> (a.getKey() == b.getKey() ? a.getValue() - b.getValue() : b.getKey() - a.getKey()));
        int res = Integer.MIN_VALUE;
        for (int[] point : points) {
            while (!pq.isEmpty() && point[0] - pq.peek().getValue() > k) { // xj - xi -> point[0] - (point[0] in heap)
                pq.poll();
            }
            if (!pq.isEmpty()) {
                res = Math.max(res, pq.peek().getKey() + point[0] + point[1]);
            }
            pq.offer(new Pair<>(point[1] - point[0], point[0]));
        }
        return res;
    }

    public static void main(String[] args) {
        MaxValueEquation m = new MaxValueEquation();
        int[][] input = {
                {1,3},
                {2,0},
                {5,10},
                {6,-10}
        };

        System.out.println(m.findMaxValueOfEquation(input, 1));
    }
}
