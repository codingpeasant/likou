package Other;

import java.util.Arrays;

// https://leetcode.com/problems/merge-sorted-array/
public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1; // go from the largest
        while (i >= 0 && j >= 0) {
            nums1[k--] = nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }

    public static void main(String[] args) {
        MergeSortedArray m = new MergeSortedArray();
        int[] num1 = {1,2,3,0,0,0};
        int[] num2 = {2,5,6};
        m.merge(num1, 3, num2, 3);
        System.out.println(Arrays.toString(num1));
    }
}
