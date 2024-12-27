package DP;

import java.util.Arrays;

// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
// the minimum difficulty if start work at ith job with d days left.
// dfs is easier to understand
public class MinimumDifficultyJobSchedule {
    public int minDifficulty(int[] jobDifficulty, int D) {
        final int N = jobDifficulty.length;
        if (N < D) return -1;
        int[][] dp = new int[D][N];

        dp[0][0] = jobDifficulty[0]; // one day one job
        for (int j = 1; j < N; ++j) {
            dp[0][j] = Math.max(jobDifficulty[j], dp[0][j - 1]); // one day N jobs
        }

        for (int d = 1; d < D; ++d) { // starts from day 2
            for (int len = d; len < N; ++len) { // cannot schedule one job in 2 days
                int localMax = jobDifficulty[len];
                dp[d][len] = Integer.MAX_VALUE;
                for (int schedule = len; schedule >= d; --schedule) {
                    localMax = Math.max(localMax, jobDifficulty[schedule]);
                    dp[d][len] = Math.min(dp[d][len], dp[d - 1][schedule - 1] + localMax);
                }
            }
        }

        return dp[D - 1][N - 1];
    }

    public int minDifficultyDFS(int[] jobDifficulty, int D) {
        final int N = jobDifficulty.length;
        if (N < D) return -1;

        int[][] memo = new int[N][D + 1];
        for (int[] row : memo) Arrays.fill(row, -1);

        return dfs(D, 0, jobDifficulty, memo);
    }

    private int dfs(int d, int len, int[] jobDifficulty, int[][] memo) {
        final int N = jobDifficulty.length;
        if (d == 0 && len == N) return 0; // no job to do and no time left
        if (d == 0 || len == N) return Integer.MAX_VALUE; // either no time left but jobs exists OR job done but more time left
        if (memo[len][d] != -1) return memo[len][d]; // len = job done so far; d = days left

        int curMax = jobDifficulty[len];
        int min = Integer.MAX_VALUE;
        for (int schedule = len; schedule < N; ++schedule) {
            curMax = Math.max(curMax, jobDifficulty[schedule]);
            int temp = dfs(d - 1, schedule + 1, jobDifficulty, memo);
            if (temp != Integer.MAX_VALUE)
                min = Math.min(min, temp + curMax);
        }

        return memo[len][d] = min;
    }

    public static void main(String[] args) {
        MinimumDifficultyJobSchedule m = new MinimumDifficultyJobSchedule();
        int[] jobD = {6, 5, 4, 3, 2, 1};
        System.out.println(m.minDifficulty(jobD, 3));
        System.out.println(m.minDifficultyDFS(jobD, 3));
    }
}
