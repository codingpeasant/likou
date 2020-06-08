package DFS;

public class WordSearch {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j ++) {
                if (word.charAt(0) == board[i][j] && searchDFS(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean searchDFS(char[][]board, int i, int j, String word, int length) {
        if (length == word.length()) {
            return true;
        }

        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(length)) {
            return false;
        }

        // The same letter cell may not be used more than once.
        char temp = board[i][j];
        board[i][j] = ' ';

        boolean found = searchDFS(board, i + 1, j, word, length + 1) || searchDFS(board, i - 1, j, word, length + 1)
                || searchDFS(board, i, j + 1, word, length + 1) || searchDFS(board, i, j - 1, word, length + 1);

        board[i][j] = temp;

        return found;
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        char M[][] = new char[][]{
                {'A','B','C','E'},
                {'S','F','C','S'},
                {'A','D','E','E'}
        };

        WordSearch w = new WordSearch();
        System.out.println("Word exists: " +w.exist(M, "SEE"));
    }
}
