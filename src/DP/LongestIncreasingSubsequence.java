package DP;

import java.util.Arrays;

// https://leetcode.com/problems/longest-increasing-subsequence/
public class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            // subsequnce needs to look at all the previous values - subarray only needs to lool at i - 1
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                max = Math.max(dp[i], max);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        LongestIncreasingSubsequence mdt = new LongestIncreasingSubsequence();
        int[] sequence = {10,9,2,5,3,7,101,18};
        System.out.println("Max: " + mdt.lengthOfLIS(sequence));
    }
}
