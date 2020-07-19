package DFS;

public class WallGates {
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
        int rows = rooms.length;
        int cols = rooms[0].length;

        if (i < 0 || j < 0 || i >= rooms.length || j >= rooms.length || rooms[i][j] < distance) {
            return;
        }

        rooms[i][j] = distance;
        dfs(rooms, i + 1, j, distance + 1);
        dfs(rooms, i, j + 1, distance + 1);
        dfs(rooms, i, j - 1, distance + 1);
        dfs(rooms, i - 1, j, distance + 1);
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
