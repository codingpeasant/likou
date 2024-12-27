package DFS;

// https://leetcode.com/problems/max-area-of-island/
public class MaxAreaOfIsland {
    public int maxAreaOfIsland(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;

        int max = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    max = Math.max(max, getMax(grid, i, j));
                }
            }
        }

        return max;
    }

    private int getMax(int[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != 1) {
            return 0;
        }

        grid[i][j] = 0;
        int count = 1;

        count += getMax(grid, i + 1, j);
        count += getMax(grid, i - 1, j);
        count += getMax(grid, i, j - 1);
        count += getMax(grid, i, j + 1);

        return count;
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        int M[][] = new int[][]{
                {1, 1, 1, 0, 0},
                {1, 0, 1, 0, 0},
                {0, 0, 0, 1, 1},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1}
        };
        MaxAreaOfIsland I = new MaxAreaOfIsland();
        System.out.println("Max area of islands is: " + I.maxAreaOfIsland(M));
    }
}
