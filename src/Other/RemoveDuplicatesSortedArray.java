package Other;

import java.util.Arrays;

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
public class RemoveDuplicatesSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int res = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[res++] = nums[i];
            }
        }
        return res;
    }

    public int removeDuplicates2(int[] A) {
        if (A.length == 0) return 0;
        int j = 0;
        for (int i = 0; i < A.length; i++)
            if (A[i] != A[j]) A[++j] = A[i];
        return ++j;
    }

    public static void main(String[] args) {
        RemoveDuplicatesSortedArray r = new RemoveDuplicatesSortedArray();
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        System.out.println(r.removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }
}
