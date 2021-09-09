package DP;

// https://leetcode.com/problems/maximum-product-subarray/
public class MaxProductSubarray {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }
        int maxPossible = nums[0];
        int minPossible = nums[0];
        int ans = maxPossible;

        for(int i = 1; i < nums.length; i++){
            int a = nums[i] * maxPossible;
            int b = nums[i] * minPossible;
            int c = nums[i];
            maxPossible = Math.max(a, Math.max(b,c)) ;
            minPossible = Math.min(a, Math.min(b,c)) ;
            ans  = Math.max(ans, maxPossible);
        }

        return ans;
    }

    public int maxProductDP(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }

        // needs to track both min and max to find the next max or min
        int[] dpMax = new int[nums.length]; // max ending here - i must be included as the ending element
        int[] dpMin = new int[nums.length]; // min ending here - i must be included as the ending element

        dpMax[0] = nums[0];
        dpMin[0] = nums[0];
        int maxProduct = nums[0];

        for (int i = 1; i < nums.length ; i++) {
            // need to try to get the possible products
            int possibleProductA = nums[i] * dpMax[i - 1];
            int possibleProductB = nums[i] * dpMin[i - 1];

            // just use the current num or a product with the previous max or min
            dpMax[i] = Math.max(nums[i], Math.max(possibleProductA, possibleProductB));
            dpMin[i] = Math.min(nums[i], Math.min(possibleProductA, possibleProductB));

            maxProduct = Math.max(maxProduct, dpMax[i]);
        }

        return maxProduct;
    }

    public static void main(String[] args) {
        MaxProductSubarray mdt = new MaxProductSubarray();
        int[] sequence = {-2,1,-3,4,-1,2,1,-5,-4};
        System.out.println("MaxSub Product: " + mdt.maxProduct(sequence) + "/" + mdt.maxProductDP(sequence));
    }
}
