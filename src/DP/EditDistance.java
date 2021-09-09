package DP;

// https://leetcode.com/problems/edit-distance/
// https://leetcode.com/problems/edit-distance/discuss/25849/Java-DP-solution-O(nm)
public class EditDistance {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        int[][] cost = new int[m + 1][n + 1]; // first row/col is empty string
        for (int i = 0; i <= m; i++)
            cost[i][0] = i;
        for (int i = 1; i <= n; i++)
            cost[0][i] = i;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (word1.charAt(i) == word2.charAt(j))
                    cost[i + 1][j + 1] = cost[i][j];
                else {
                    int a = cost[i][j]; // replace
                    int b = cost[i][j + 1]; // delete
                    int c = cost[i + 1][j]; // insert
                    cost[i + 1][j + 1] = a < b ? (Math.min(a, c)) : (Math.min(b, c));
                    cost[i + 1][j + 1]++;
                }
            }
        }
        return cost[m][n];
    }

    public static void main(String[] args) {
        EditDistance ed = new EditDistance();
        System.out.println(ed.minDistance("intention", "execution"));
    }

}
