package DP;

// https://leetcode.com/problems/climbing-stairs/
// both dp and dfs have the same logic, but use different ways to build the final result
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

        // when n - 1, you can step up by 1; when n -2, you can step up by 2; so add the previous 2 steps' ways together
        return climbStairsDFS(n - 1) + climbStairsDFS(n - 2);
    }

    public static void main(String[] args) {
        ClimbingStairs c = new ClimbingStairs();
        int input = 5;
        System.out.println("Ways to climb: " + c.climbStairsDFS(input) + "/" + c.climbStairs(input));
    }
}
