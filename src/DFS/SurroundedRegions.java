package DFS;

// https://leetcode.com/problems/surrounded-regions/
// We search for invalid candidates (and exclude them) rather than search for valid candidates.
public class SurroundedRegions {
    private static final int[][] dirs = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
    };

    public void solve(char[][] board) {
        if (board.length == 0)
            return;

        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                markNotSurrounded(i, 0, board);
            }

            if (board[i][n - 1] == 'O') {
                markNotSurrounded(i, n -1, board);
            }
        }

        for (int i = 0; i < n; i++) {
            if (board[0][i] == 'O') {
                markNotSurrounded(0, i, board);
            }

            if (board[m-1][i] == 'O') {
                markNotSurrounded(m-1, i, board);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }

                if (board[i][j] == '*') {
                    board[i][j] = 'O';
                }
            }
        }

    }

    // Mark 'O' not surrounded by 'X' as '*'
    private void markNotSurrounded(int x, int y, char[][] board) {
        board[x][y] = '*';
        for(int[] dir: dirs) {
            int nextX = x + dir[0];
            int nextY = y + dir[1];

            if (nextX < board.length && nextX >= 0 && nextY < board[0].length && nextY >= 0 && board[nextX][nextY] == 'O') {
                markNotSurrounded(nextX, nextY, board);
            }
        }
    }

    public static void main(String[] args) {
        SurroundedRegions s = new SurroundedRegions();
        char[][] board = {
                {'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}
        };

        s.solve(board);
        System.out.println(board);
    }
}
