package Binary;

// https://leetcode.com/problems/search-in-rotated-sorted-array/
public class SearchRotatedSortedArray {
    public int search(int[] nums, int target) {
        int smallestIndex = findSmallestIndex(nums);

        if (nums[smallestIndex] == target) {
            return smallestIndex;
        }
        int low = 0;
        int high = nums.length - 1;
        if (target <= nums[nums.length - 1]) {
            low = smallestIndex + 1;
        } else {
            high = smallestIndex - 1;
        }

        while (low <= high) { // standard binary search
            int mid = (low + high) / 2;
            if (nums[mid] == target) return mid;
            else if (target > nums[mid]) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    public int findSmallestIndex(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        while (high > low) {
             int mid = (high + low) / 2;
             if (nums[mid] > nums[high]) {
                 low = mid + 1;
             } else {
                 high = mid;
             }
        }
        return low;
    }

    public static void main(String[] args) {
        SearchRotatedSortedArray s = new SearchRotatedSortedArray();
        int nums[] = {4,5,6,7,8,0,1,2,3};
        System.out.println("index is: " + s.search(nums, 3));
    }
}
