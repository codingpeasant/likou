package BackTrack;

// https://leetcode.com/problems/unique-paths-iii/
public class UniquePaths3 {
    private int empty;
    public int uniquePathsIII(int[][] grid) {
        int m = grid.length, n = grid[0].length, sx = 0, sy = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) empty++; // track how many cell it needs to traverse
                else if (grid[i][j] == 1) { // find starting
                    sx = i;
                    sy = j;
                }
            }
        }

        return dfs(grid, sx, sy, new boolean[m][n]);
    }

    private int dfs(int[][] grid, int x, int y, boolean[][] visited) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == -1 || visited[x][y])
            return 0; // this path doesn't work
        if (grid[x][y] == 2) { // destination met
            if (empty == 0) return 1; // all cells traversed
            else return 0; // terminate early
        }

        int res = 0;
        visited[x][y] = true;
        if (grid[x][y] == 0) empty--; // when grid[x][y] == 1, do nothing
        res += dfs(grid, x + 1, y, visited);
        res += dfs(grid, x - 1, y, visited);
        res += dfs(grid, x, y + 1, visited);
        res += dfs(grid, x, y - 1, visited);
        visited[x][y] = false;
        if (grid[x][y] == 0) empty++;

        return res;
    }

    public static void main(String[] args) {
        UniquePaths3 u = new UniquePaths3();
        int[][] grid = {
                {1,-1},
                {0,2}
        };
        System.out.println(u.uniquePathsIII(grid));
    }
}
