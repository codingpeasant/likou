package Binary;

// https://leetcode.com/problems/median-of-two-sorted-arrays/
public class MedianTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        int num1Len = nums1.length;
        int num2Len = nums2.length;
        int left = 0;
        int right = num1Len;
        while (left <= right) {
            int firstPartNum1 = (left + right) / 2; // assume the mid of nums1
            int firstPartNum2 = (num1Len + num2Len + 1) / 2 - firstPartNum1; // given the mid of nums1, calculate the length for num2; len(firstPart) == len(secondPart)
            int num1FirstPartLargest = firstPartNum1 == 0 ? Integer.MIN_VALUE : nums1[firstPartNum1 - 1];
            int num1SecondPartSmallest = firstPartNum1 == num1Len ? Integer.MAX_VALUE : nums1[firstPartNum1];
            int num2FirstPartLargest = firstPartNum2 == 0 ? Integer.MIN_VALUE : nums2[firstPartNum2 - 1];
            int num2SecondPartSmallest = firstPartNum2 == num2Len ? Integer.MAX_VALUE : nums2[firstPartNum2];
            // to make sure the first part of both arrays are strictly smaller than the second part
            if (num1FirstPartLargest <= num2SecondPartSmallest && num2FirstPartLargest <= num1SecondPartSmallest) {
                if ((num1Len + num2Len) % 2 == 0) {
                    return ((double) Math.max(num1FirstPartLargest, num2FirstPartLargest) + Math.min(num1SecondPartSmallest, num2SecondPartSmallest)) / 2;
                } else {
                    return Math.max(num1FirstPartLargest, num2FirstPartLargest);
                }
            } else if (num1FirstPartLargest > num2SecondPartSmallest) {
                right = firstPartNum1 - 1;
            } else {
                left = firstPartNum1 + 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        MedianTwoSortedArrays m = new MedianTwoSortedArrays();
        int[] num1 = {1,2,4};
        int[] num2 = {3,5,6,7};
        System.out.println(m.findMedianSortedArrays(num1, num2));
    }

}
