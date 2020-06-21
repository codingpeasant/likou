package SlidingWindow;

public class MaxSubarray {
    public int maxSubArray(int[] nums) {
        int currSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currSum = Math.max(currSum + nums[i], nums[i]);
            if (currSum > maxSum) {
                maxSum = currSum;
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        MaxSubarray mdt = new MaxSubarray();
        int[] sequence = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println("MaxSub: " + mdt.maxSubArray(sequence));
    }
}
