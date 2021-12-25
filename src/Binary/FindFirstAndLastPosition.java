package Binary;

import java.util.Arrays;

// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
public class FindFirstAndLastPosition {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[2];
        res[0] = findFirst(nums, target);
        res[1] = findLast(nums, target);
        return res;
    }

    private int findFirst(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else { // found the target
                right = mid - 1;
            }
        }

        if (left >= nums.length || nums[left] != target)
            return -1;
        return left;
    }

    private int findLast(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] == target) {
                // 别返回，锁定右侧边界
                left = mid + 1;
            }
        }
        // 最后要检查 right 越界的情况
        if (right < 0 || nums[right] != target)
            return -1;
        return right;
    }

    private int binarySearchLeftOrFloor(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int floor = -1;
        while (left <= right) {
            int mid = left + (right - left) /2 ;
            if (nums[mid] < target) {
                floor = mid;
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                right = mid - 1;
            }
        }

        if (target != nums[left]) {
            return floor;
        }
        return left;
    }

    public static void main(String[] args) {
        FindFirstAndLastPosition f = new FindFirstAndLastPosition();
        int[] nums = {5,7,7,8,8,10};
        System.out.println(Arrays.toString(f.searchRange(nums, 5)));
        System.out.println(f.binarySearchLeftOrFloor(nums, 9));
    }
}
