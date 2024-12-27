package Heap;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

// https://leetcode.com/problems/k-closest-points-to-origin/
public class KClosestPoints {
    public int[][] kClosest(int[][] points, int K) {
        Queue<int[]> minHeap = new PriorityQueue<>(
                ((o1, o2) -> (o1[0] * o1[0] + o1[1] * o1[1]) - (o2[0] * o2[0] + o2[1] * o2[1]))
        );

        minHeap.addAll(Arrays.asList(points));

        int[][] results = new int[K][2];
        for (int i = 0; i < K; i++) {
            results[i] = minHeap.poll();
        }

        return results;
    }

    public static void main(String[] args) {
        KClosestPoints k = new KClosestPoints();
        int[][] points = {{3, 3}, {5, -1}, {-2, 4}};

        int[][] results = k.kClosest(points, 2);
        for (int i = 0; i < 2; i++) {
            System.out.println(results[i][0] + ", " + results[i][1]);
        }

    }
}
