package DP;

// https://leetcode.com/problems/house-robber/
public class HouseRob {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        int[] dp = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                dp[i] = nums[i];
            } else if (i == 1) {
                dp[i] = Math.max(dp[i - 1], nums[i]);
            } else {
                dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]); // rob current or skip current
            }
        }

        return dp[nums.length - 1];
    }

    public static void main(String args[]) {
        HouseRob h = new HouseRob();
        int[] input = {200,7,9,100,1};
        System.out.println("Max money: " + h.rob(input));
    }
}
