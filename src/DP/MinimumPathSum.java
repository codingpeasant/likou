package DP;

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

    public static void main(String[] args) {
        int M[][] = new int[][]{
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };

        MinimumPathSum w = new MinimumPathSum();
        System.out.println("Min Path Sum: " + w.minPathSum(M));
    }
}
