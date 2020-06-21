package DP;

public class UniquePaths {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i < m; i++) {
            dp[i][1]=1;
        }

        for (int i = 1; i < m; i++) {
            dp[1][n]=1;
        }

        for(int i=2;i<=m;i++)
        {
            for(int j=2;j<=n;j++)
            {
                dp[i][j]=(dp[i-1][j]+dp[i][j-1]);      //just add the number of ways from prev row and prev
                //colm

            }
        }
        return dp[m][n];
    }

    public static void main(String[] args) {
        UniquePaths u = new UniquePaths();
        System.out.println("Unique Path: " + u.uniquePaths(3, 3));
    }
}
