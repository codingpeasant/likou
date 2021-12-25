package DFS;

import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/pacific-atlantic-water-flow/
public class PacificAtlanticWaterFlow {
    // size: 4 * 2
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> res = new LinkedList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return res;
        }

        int n = matrix.length;
        int m = matrix[0].length;

        boolean[][] pacific = new boolean[n][m];
        boolean[][] atlantic = new boolean[n][m];

        // starts from 4 edges inwards
        for(int i=0; i<n; i++){
            dfs(matrix, pacific, Integer.MIN_VALUE, i, 0);
            dfs(matrix, atlantic, Integer.MIN_VALUE, i, m-1);
        }
        for(int i=0; i<m; i++){
            dfs(matrix, pacific, Integer.MIN_VALUE, 0, i);
            dfs(matrix, atlantic, Integer.MIN_VALUE, n-1, i);
        }

        // cells flowed by both oceans
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(new int[] {i, j});
                }
        return res;
    }

    public void dfs(int[][] matrix, boolean[][] visited, int height, int x, int y) {
        int n = matrix.length;
        int m = matrix[0].length;

        // water flows from the oceans to all the cells backward
        // the current cell should be higher than the previous for water to flow backward
        if (x < 0 || x >= n || y < 0 || y >= m || visited[x][y] || matrix[x][y] < height) {
            return;
        }

        visited[x][y] = true;
        for (int[] dir : dirs) {
            dfs(matrix, visited, matrix[x][y], x + dir[0], y + dir[1]);
        }
    }

    public static void main(String args[]) {
        PacificAtlanticWaterFlow p = new PacificAtlanticWaterFlow();
        int[][] input = {
                {1,2,2,3,5},
                {3,2,3,4,4},
                {2,4,5,3,1},
                {6,7,1,4,5},
                {5,1,1,2,4}
        };
        p.pacificAtlantic(input).forEach(arr -> System.out.println(arr[0] + "," + arr[1]));
    }
}
