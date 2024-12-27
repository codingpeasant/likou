package DP;

// https://leetcode.com/problems/maximum-subarray/
// https://leetcode.com/problems/maximum-subarray/discuss/20211/Accepted-O(n)-solution-in-java

public class MaxSubarray {
    // Kadane's algorithm
    public int maxSubArray(int[] nums) {
        int currSum = nums[0]; // max ending here
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currSum = Math.max(currSum + nums[i], nums[i]);
            if (currSum > maxSum) {
                maxSum = currSum;
            }
        }
        return maxSum;
    }

    // this is actually the same with above but using O(n) extra space
    public int maxSubArrayDP(int[] nums) {
        int maxSum = nums[0];

        int[] dp = new int[nums.length]; // max ending here - i must be included as the ending element
        dp[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
            maxSum = Math.max(maxSum, dp[i]);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        MaxSubarray mdt = new MaxSubarray();
        int[] sequence = {-2,1,-3,4,-1,2,1,-5,10};
        System.out.println("MaxSub: " + mdt.maxSubArray(sequence) + "/" + mdt.maxSubArrayDP(sequence));
    }
}
