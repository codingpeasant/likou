package BackTrack;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/n-queens/
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                board[i][j] = '.';
        List<List<String>> res = new ArrayList<>();
        dfs(board, 0, res);
        return res;
    }

    private void dfs(char[][] board, int row, List<List<String>> res) {
        if(row == board.length) {
            res.add(construct(board));
            return;
        }

        for(int col = 0; col < board.length; col++) { // from left to right
            if(validate(board, row, col)) {
                board[row][col] = 'Q';
                dfs(board, row + 1, res);
                board[row][col] = '.';
            }
        }
    }

    private boolean validate(char[][] board, int row, int col) {
        int n = board.length;

        // same col
        for (int i = 0; i < n; i++) {
            if (board[i][col] == 'Q')
                return false;
        }

        // left up
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q')
                return false;
        }

        // right up
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q')
                return false;
        }

        return true;
    }

    private List<String> construct(char[][] board) {
        List<String> res = new LinkedList<>();
        for(int i = 0; i < board.length; i++) {
            String s = new String(board[i]);
            res.add(s);
        }
        return res;
    }

    public static void main(String[] args) {
        NQueens n = new NQueens();
        List<List<String>> res = n.solveNQueens(4);
        res.forEach(board -> System.out.println(board.toString()));
    }
}
