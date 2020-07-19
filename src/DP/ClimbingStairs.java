package DP;

public class ClimbingStairs {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];

        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    public int climbStairsDFS(int n) {
        if (n == 1) {
            return 1;
        }

        if (n == 2) {
            return 2;
        }

        return climbStairsDFS(n - 1) + climbStairsDFS(n - 2);
    }

    public static void main(String[] args) {
        ClimbingStairs c = new ClimbingStairs();
        int input = 5;
        System.out.println("Ways to climb: " + c.climbStairsDFS(input) + "/" + c.climbStairs(input));
    }
}
