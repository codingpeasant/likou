package Other;

import java.util.Arrays;

// https://leetcode.com/problems/squares-of-a-sorted-array/
public class SquaresSortedArray {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) { // from the largest to the smallest
            if (Math.abs(nums[i]) > Math.abs(nums[j])) {
                result[p] = nums[i] * nums[i];
                i++;
            } else {
                result[p] = nums[j] * nums[j];
                j--;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        SquaresSortedArray s = new SquaresSortedArray();
        int[] input = {-4, -1, 0, 0, 3, 10};
        System.out.println(Arrays.toString(s.sortedSquares(input)));
    }
}
