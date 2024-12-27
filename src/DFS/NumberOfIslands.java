package DFS;

// https://leetcode.com/problems/number-of-islands/
public class NumberOfIslands {
    public int numIslands(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;

        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    merge(grid, i, j);
                    count++;
                }
            }
        }

        return count;
    }

    // merge all the nodes horizontally and vertically
    public void merge(int[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != 1) {
            return;
        }

        grid[i][j] = 0;
        merge(grid, i - 1, j);
        merge(grid, i + 1, j);
        merge(grid, i, j + 1);
        merge(grid, i, j - 1);
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        int M[][] = new int[][]{
                {1, 1, 1, 1, 1},
                {0, 0, 0, 0, 0},
                {1, 0, 0, 1, 1},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1}
        };
        NumberOfIslands I = new NumberOfIslands();
        System.out.println("Number of islands is: " + I.numIslands(M));
    }
}
