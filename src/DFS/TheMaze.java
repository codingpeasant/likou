package DFS;

// https://leetcode.ca/2017-04-03-490-The-Maze/
public class TheMaze {
    // size: 4 * 2
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        return dfs(maze, start, destination, visited);
    }

    private boolean dfs(int[][] maze, int[] cur, int[] dest, boolean[][] visited) {
        if (cur[0] == dest[0] && cur[1] == dest[1]) {
            return true;
        }

        if (visited[cur[0]][cur[1]]) {
            return false;
        }

        visited[cur[0]][cur[1]] = true;

        for (int i = 0; i < dirs.length; i++) {
            int x = cur[0], y = cur[1];
            while (x >= 0 && x < maze.length && y >= 0 && y < maze[0].length && maze[x][y] == 0) {
                x = x + dirs[i][0];
                y = y + dirs[i][1];
            }

            x = x - dirs[i][0];
            y = y - dirs[i][1];

            if (!visited[x][y] && dfs(maze, new int[]{x, y}, dest, visited)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        TheMaze m = new TheMaze();
        int[][] input = {
                {0,0,1,0,0},
                {0,0,0,0,0},
                {0,0,0,1,0},
                {1,1,0,1,1},
                {0,0,0,0,0}
        };

        System.out.println(m.hasPath(input, new int[]{0,4}, new int[]{4,4}));
    }
}
