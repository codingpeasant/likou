package SlidingWindow;

public class MaxProductSubarray {
    public int maxProduct(int[] nums) {
        if(nums==null || nums.length==0){
            return 0;
        }
        int maxPossible = nums[0];
        int minPossible = nums[0];
        int ans = maxPossible;

        for(int i=1;i<nums.length;i++){
            int a = nums[i]*maxPossible;
            int b = nums[i]*minPossible;
            int c = nums[i];
            maxPossible = Math.max(a,Math.max(b,c)) ;
            minPossible = Math.min(a,Math.min(b,c)) ;
            ans  = Math.max(ans,maxPossible);
        }

        return ans;
    }

    public static void main(String[] args) {
        MaxProductSubarray mdt = new MaxProductSubarray();
        int[] sequence = {-2,1,-3,4,-1,2,1,-5,-4};
        System.out.println("MaxSub Product: " + mdt.maxProduct(sequence));
    }
}
