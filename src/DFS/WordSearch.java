package DFS;

import java.util.HashMap;

// https://leetcode.com/problems/word-search/
public class WordSearch {
    class TrieNode {
        HashMap<Character, TrieNode> children = new HashMap<>();
        char letter;
        String word;
    }

    private TrieNode buildTrie(String word) {
        TrieNode root = new TrieNode();
        TrieNode p = root;
        for (char ch : word.toCharArray()) {
            if (p.children.get(ch) == null) {
                TrieNode newNode = new TrieNode();
                newNode.letter = ch;
                p.children.put(ch, newNode);
            }
            p = p.children.get(ch);
        }
        p.word = word;

        return root;
    }

    public boolean existTrie(char[][] board, String word) {
        TrieNode root = buildTrie(word);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (root.children.containsKey(board[i][j]) && searchTrieDFS(board, i, j, root)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean searchTrieDFS(char[][] board, int i, int j, TrieNode p) {
        if (p.word != null) {
            return true;
        }

        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || !p.children.containsKey(board[i][j])) {
            return false;
        }

        TrieNode child = p.children.get(board[i][j]);
        char temp = board[i][j];
        board[i][j] = ' ';

        boolean found = searchTrieDFS(board, i + 1, j, child) || searchTrieDFS(board, i - 1, j, child)
                || searchTrieDFS(board, i, j + 1, child) || searchTrieDFS(board, i, j - 1, child);

        board[i][j] = temp;

        return found;

    }

    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (word.charAt(0) == board[i][j] && searchDFS(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean searchDFS(char[][] board, int i, int j, String word, int length) {
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
                {'A', 'B', 'C', 'E'},
                {'S', 'F', 'C', 'S'},
                {'A', 'D', 'E', 'E'}
        };

        WordSearch w = new WordSearch();
        System.out.println("Word exists: " + w.exist(M, "FCSE"));
        System.out.println(w.existTrie(M, "FCSE"));
    }
}
