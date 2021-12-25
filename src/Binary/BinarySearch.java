package Binary;

// https://leetcode.com/problems/binary-search/
public class BinarySearch {
    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;

        while (i <= j) {
            int mid = i + (j - i)/2;
            if (nums[mid] > target) {
                j = mid - 1;
            } else if (nums[mid] < target) {
                i = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch b = new BinarySearch();
        int[] input = {-1,0,3,5,9,12};
        System.out.println(b.search(input, -1));
    }
}
