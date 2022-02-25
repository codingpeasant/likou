package DP;

// https://leetcode.com/problems/longest-palindromic-substring/
public class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        boolean[][] fromTo = new boolean[s.length()][s.length()];
        int length = 1;
        int start = 0;

        for (int i = 0; i < s.length(); i++) {
            fromTo[i][i] = true;
        }

        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i + 1; j <= s.length() - 1; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i == 1 || fromTo[i + 1][j - 1])) {
                    int curLen = j - i + 1;
                    fromTo[i][j] = true;
                    if (curLen > length) {
                        length = curLen;
                        start = i;
                    }
                }
            }
        }

        return s.substring(start, start + length);
    }

    int start = 0;
    int length = 1;
    public String longestPalindromeDFS(String s) {
        if (s.length() == 0) return "";
        helper(s, 0, s.length() - 1, new int[s.length()][s.length()]);
        return s.substring(start, start + length);
    }

    private boolean helper(String s, int i, int j, int[][] mem) {
        if (i == j) return true;
        if (i > j) return false;
        if (mem[i][j] == 1) {
            return true;
        }
        if (mem[i][j] == -1) {
            return false;
        }

        if (s.charAt(i) == s.charAt(j) && (j - i == 1 || helper(s, i + 1, j - 1, mem))) {
            int curLen = j - i + 1;
            if (curLen > length) {
                start = i;
                length = curLen;
            }
            mem[i][j] = 1;
            return true;
        } else {
            mem[i][j] = -1;
            helper(s, i, j - 1, mem);
            helper(s, i + 1, j, mem);
        }
        return false;
    }

    public static void main(String[] args) {
        String input = "babad";
        LongestPalindromicSubstring l = new LongestPalindromicSubstring();
        System.out.println(l.longestPalindrome(input));
        System.out.println(l.longestPalindromeDFS(input));
    }
}
