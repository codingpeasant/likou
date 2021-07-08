package DFS;

public class TheMaze2 {
    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int[][] distance = new int[maze.length][maze[0].length];
        for (int i = 0; i < maze.length; i++) {
            for (int j = 0; j < maze[0].length; j++) {
                distance[i][j] = Integer.MAX_VALUE;
            }
        }
        distance[start[0]][start[1]] = 0;
        dfs(maze, start, destination, distance);
        return distance[destination[0]][destination[1]] == Integer.MAX_VALUE ? -1 : distance[destination[0]][destination[1]];
    }

    private void dfs(int[][] maze, int[] start, int[] destination, int[][] distance) {
        if (start[0] == destination[0] && start[1] == destination[1]) return;
        for (int[] d : directions) {
            int row = start[0], col = start[1];
            while (row >= 0 && row < maze.length && col >= 0 && col < maze[0].length && maze[row][col] == 0) {
                row += d[0];
                col += d[1];
            }
            row -= d[0];
            col -= d[1];
            int[] newStart = {row, col};
            int dis = distance[start[0]][start[1]] + Math.abs(start[0] - row) + Math.abs(start[1] - col);
            if (distance[row][col] > dis) {
                distance[row][col] = dis;
                dfs(maze, newStart, destination, distance);
            }
        }
    }

    public static void main(String[] args) {
        TheMaze2 m = new TheMaze2();
        int[][] input = {
                {0,0,1,0,0},
                {0,0,0,0,0},
                {0,0,0,1,0},
                {1,1,0,1,1},
                {0,0,0,0,0}
        };

        System.out.println(m.shortestDistance(input, new int[]{0,4}, new int[]{4,4}));
    }
}
