package DFS;

// https://leetcode.ca/2016-09-11-286-Walls-and-Gates/
public class WallGates {
    private static final int[][] DIRS = new int[][]{
            {-1,0},
            {1,0},
            {0, -1},
            {0,1}
    };
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0) return;
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    dfs(rooms, i, j, 0);
                }
            }
        }
    }

    private void dfs(int[][] rooms, int i, int j, int distance) {
        if (i < 0 || j < 0 || i >= rooms.length || j >= rooms.length || rooms[i][j] < distance) { // found a smaller one before
            return;
        }
        // current distance is smaller
        rooms[i][j] = distance;
        for (int[] dir: DIRS) {
            dfs(rooms, i + dir[0], j + dir[1], distance + 1);
        }
    }

    public static void main(String[] args) {
        int M[][] = new int[][]{
                {100, 100, 100},
                {100, -1, -1},
                {100, 0, 100},
        };

        WallGates w = new WallGates();
        w.wallsAndGates(M);
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                System.out.print(M[i][j] + ", ");
            }
        }

    }
}
