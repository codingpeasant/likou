package SlidingWindow;

public class MinimumSizeSubarraySum {
    public int minSubArrayLen(int s, int[] nums) {
        if(nums == null) return 0;
        int ans = Integer.MAX_VALUE;
        int sum = 0;
        int localAns = 0;
        for(int i = 0, j = 0;i< nums.length;i++){ //i is the faster pointer, j is the slower pointer
            sum += nums[i];
            localAns++;
            while(sum >= s){
                ans = Math.min(ans,localAns);// update global ans.
                localAns--;
                sum -= nums[j];
                j++; // move the slower pointer forward and decrease the related nums[j], at the same time localAns will be decreased by 1.
            }
        }
        return (ans == Integer.MAX_VALUE) ? 0: ans;
    }

    public static void main(String[] args) {
        MinimumSizeSubarraySum m = new MinimumSizeSubarraySum();
        int[] input = {2,3,1,2,6,3};
        System.out.println("Min length: " + m.minSubArrayLen(7, input));
    }
}
