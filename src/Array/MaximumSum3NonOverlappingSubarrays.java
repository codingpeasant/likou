package Array;

import java.util.Arrays;

// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
public class MaximumSum3NonOverlappingSubarrays {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        // windowSums is an array of sums of windows; windowSums[0] = nums[0]+nums[1]...num[k-1]
        int[] windowSums = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length - k; i++) {
            int curSum = 0;
            for (int j = 0; j < k; j++) {
                curSum += nums[i + j];
            }
            windowSums[i] = curSum;
        }

        int[] left = new int[windowSums.length];
        int best = 0;
        for (int i = 0; i < windowSums.length; i++) {
            if (windowSums[i] > windowSums[best]) best = i;
            left[i] = best;
        }

        int[] right = new int[windowSums.length];
        best = windowSums.length - 1;
        for (int i = windowSums.length - 1; i >= 0; i--) {
            if (windowSums[i] >= windowSums[best]) {
                best = i;
            }
            right[i] = best;
        }

        int[] ans = new int[]{-1, -1, -1};
        for (int j = k; j < windowSums.length - k; j++) {
            int i = left[j - k], l = right[j + k];
            if (ans[0] == -1 || windowSums[i] + windowSums[j] + windowSums[l] > windowSums[ans[0]] + windowSums[ans[1]] + windowSums[ans[2]]) {
                ans[0] = i;
                ans[1] = j;
                ans[2] = l;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        MaximumSum3NonOverlappingSubarrays m = new MaximumSum3NonOverlappingSubarrays();
        int[] input = {1, 2, 1, 2, 6, 7, 5, 1};
        int k = 2;
        System.out.println(Arrays.toString(m.maxSumOfThreeSubarrays(input, k)));
    }
}
