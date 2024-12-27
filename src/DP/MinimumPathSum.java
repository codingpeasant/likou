package DP;

import java.util.*;

// https://leetcode.com/problems/minimum-path-sum/
public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        // allow change the input grid
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (i == 0 && j != 0) grid[i][j] += grid[i][j - 1];
                if (j == 0 && i != 0) grid[i][j] += grid[i - 1][j];
                if (i != 0 && j != 0) grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }

        return grid[grid.length - 1][grid[0].length - 1];
    }

    public int minPathSum1(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] minSumTo = new int[m][n];
        minSumTo[0][0] = grid[0][0];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j != 0) {
                    minSumTo[i][j] = minSumTo[i][j - 1] + grid[i][j];
                }

                if (i != 0 && j == 0) {
                    minSumTo[i][j] = minSumTo[i - 1][j] + grid[i][j];
                }

                if (i != 0 && j != 0) {
                    minSumTo[i][j] = grid[i][j] + Math.min(minSumTo[i][j - 1], minSumTo[i - 1][j]);
                }
            }
        }
        return minSumTo[m - 1][n - 1];

    }

    private List<int[]> getNeighbors(int m, int n, int[] coordinate) {
        List<int[]> neighbors = new ArrayList<>();
        if (coordinate[1] == n - 1 && coordinate[0] < m - 1) {
            neighbors.add(new int[]{coordinate[0] + 1, coordinate[1]});
            return neighbors;
        }

        if (coordinate[0] == m - 1 && coordinate[1] < n - 1) {
            neighbors.add(new int[]{coordinate[0], coordinate[1] + 1});
            return neighbors;
        }

        if (coordinate[0] == m - 1 && coordinate[1] == n - 1) {
            return neighbors;
        }

        neighbors.add(new int[]{coordinate[0] + 1, coordinate[1]});
        neighbors.add(new int[]{coordinate[0], coordinate[1] + 1});
        return neighbors;
    }

    public int minPathSumDijkstra(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        minHeap.add(new int[]{0, 0, grid[0][0]}); // [i,j,dist] from dummy original node

        while (!minHeap.isEmpty()) {
            int[] currentNode = minHeap.poll();
            int row = currentNode[0];
            int col = currentNode[1];
            int curDist = currentNode[2];
            if (visited[row][col]) continue;
            if (row == m - 1 && col == n - 1) {
                return curDist;
            }
            visited[row][col] = true;

            for (int[] neighbor : getNeighbors(m, n, new int[]{row, col})) {
                int newRow = neighbor[0];
                int newCol = neighbor[1];
                int newDist = curDist + grid[newRow][newCol];
                minHeap.add(new int[]{newRow, newCol, newDist});
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int M[][] = new int[][]{
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        MinimumPathSum w = new MinimumPathSum();
        System.out.println("Min Path Sum: " + w.minPathSum1(M));
        System.out.println("Min Path Sum: " + w.minPathSumDijkstra(M));
        System.out.println("Min Path Sum: " + w.minPathSum(M));

    }
}
