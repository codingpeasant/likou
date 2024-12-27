package DP;

// https://leetcode.com/problems/unique-paths/
public class UniquePaths {
    public int uniquePaths(int m, int n) {
        int[][] uniquePath = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            uniquePath[i][1] = 1;
        }

        for (int i = 1; i <= n; i++) {
            uniquePath[1][i] = 1;
        }

        for (int i = 2; i <= m; i++) {
            for (int j = 2; j <= n; j++) {
                uniquePath[i][j] = uniquePath[i - 1][j] + uniquePath[i][j - 1];
            }
        }

        return uniquePath[m][n];
    }

    public static void main(String[] args) {
        UniquePaths u = new UniquePaths();
        System.out.println("Unique Path: " + u.uniquePaths(3, 3));
    }
}
