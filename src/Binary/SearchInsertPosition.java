package Binary;

public class SearchInsertPosition {
    public int findMin(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        SearchInsertPosition s = new SearchInsertPosition();
        int nums[] = {0,1,2,3,4,5,6,7,8};
        System.out.println(s.findMin(nums, 4));
    }
}
