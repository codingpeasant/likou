package Array;

// https://leetcode.com/problems/product-of-array-except-self/
// prefix array
public class ProductArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        // Left is an array containing the left products
        // i.e: left[i] = nums[0] * .... * nums[i-1]  * nums[i]
        int[] left = new int[nums.length];

        // Right is an array containing the array products
        //i.e: right[i] = nums[i] * nums[i+1]  * .... * nums[len(nums)]
        int[] right = new int[nums.length];

        // left[i] = left[i-1] * nums[i-1]
        left[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        // right[i] = right[i+1] * nums[i+1]
        right[nums.length - 1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        int[] product = new int[nums.length];
        for (int i = 0; i < product.length; i++) {
            product[i] = left[i] * right[i];
        }

        return product;
    }

    public static void main(String[] args) {
        ProductArrayExceptSelf p = new ProductArrayExceptSelf();
        int[] input = {1, 2, 3, 4, 5, 6, 7, 8};
        int[] products = p.productExceptSelf(input);
        for (int product :
                products) {
            System.out.print(product + ", ");
        }
    }
}
