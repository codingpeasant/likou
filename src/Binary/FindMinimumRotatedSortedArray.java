package Binary;

// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
public class FindMinimumRotatedSortedArray {
    public int findMin(int[] nums) {
        int high = nums.length - 1;
        int low = 0;

        while (high > low) {
            int mid = (high + low) / 2;
            if (nums[mid] > nums[high]) { // pivot is on the right side
                low = mid + 1;
            } else {
                high = mid; // when it's 5,6,7,0,1,2,4, the mid is the min
            }
        }
        return low;
    }

    public static void main(String args[]) {
        FindMinimumRotatedSortedArray f = new FindMinimumRotatedSortedArray();
        int[] input = {4,5,6,7,0,1,2};
        System.out.println("the index of min: " + f.findMin(input));
    }
}
