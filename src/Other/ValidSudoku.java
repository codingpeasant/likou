package Other;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/valid-sudoku/
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        // this is not checking one cell [i][j] at a time, but checking a whole row/col and 3*3 cube
        for (int i = 0; i < 9; i++) {
            HashSet<Character> rows = new HashSet<>();
            HashSet<Character> columns = new HashSet<>();
            HashSet<Character> cube = new HashSet<>();
            for (int j = 0; j < 9; j++) { // everytime j++, it moves right and down
                if (board[i][j] != '.' && !rows.add(board[i][j]))
                    return false;
                if (board[j][i] != '.' && !columns.add(board[j][i]))
                    return false;
                int RowIndex = 3 * (i / 3); // original coordinate
                int ColIndex = 3 * (i % 3);
                if (board[RowIndex + j / 3][ColIndex + j % 3] != '.' && !cube.add(board[RowIndex + j / 3][ColIndex + j % 3]))
                    return false;
            }
        }
        return true;
    }

    public boolean isValidSudoku1(char[][] board) {
        HashSet<Character>[][] cube = new HashSet[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cube[i][j] = new HashSet<>();
            }
        }
        for (int i = 0; i < 9; i++) {
            Set<Character> rows = new HashSet<>();
            Set<Character> cols = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' && !rows.add(board[i][j])) {
                    return false;
                }

                if (board[j][i] != '.' && !cols.add(board[j][i])) {
                    return false;
                }

                int groupRow = i / 3;
                int groupCol = j / 3;
                if (board[i][j] != '.' && !cube[groupRow][groupCol].add(board[i][j])) {
                    return false;
                }
            }
        }
        return true;
    }


    public static void main(String[] args) {
        char[][] board = {
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        ValidSudoku v = new ValidSudoku();
        System.out.println(v.isValidSudoku(board));
        System.out.println(v.isValidSudoku1(board));

        for (int i = 0; i < 9; i++) {
            int x = 3 * (8 / 3) + i / 3;
            int y = 3 * (2 / 3) + i % 3;
            System.out.println(i + ";" + x + ";" + y);
        }

    }

}
