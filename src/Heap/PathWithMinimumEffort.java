package Heap;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

// https://leetcode.com/problems/path-with-minimum-effort/
public class PathWithMinimumEffort {
    int[][] dirs = new int[][]{{0,1}, {1,0}, {0,-1}, {-1,0}};

    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] dist = new int[m][n]; // distance from origin to [m][n]
        for (int i = 0; i < m; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        minHeap.offer(new int[]{0, 0, 0}); // distance, row, col
        while (!minHeap.isEmpty()) {
            int[] current = minHeap.poll();
            int distance = current[0];
            int row = current[1];
            int col = current[2];

            if (distance > dist[row][col]) {
                continue;
            }

            if (row == m - 1 && col == n - 1) { // this can guarantee the min distance being returned
                return distance;
            }

            for (int[] dir : dirs) {
                int nextRow = row + dir[0];
                int nextCol = col + dir[1];

                if (nextRow >= 0 && nextRow < m && nextCol >=0 && nextCol < n) {
                    int nextDist = Math.max(distance, Math.abs(heights[row][col] - heights[nextRow][nextCol]));
                    if (nextDist < dist[nextRow][nextCol]) {
                        dist[nextRow][nextCol] = nextDist;
                        minHeap.offer(new int[]{nextDist, nextRow, nextCol});
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        PathWithMinimumEffort p = new PathWithMinimumEffort();
        int[][] input = {
                {1,2,2},
                {3,8,2},
                {5,3,5}
        };

        System.out.println(p.minimumEffortPath(input));
    }
}
