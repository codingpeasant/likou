package Array;

import java.util.HashSet;

// https://leetcode.com/problems/first-missing-positive/
public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0) {
                min = Math.min(min, nums[i]);
                max = Math.max(max, nums[i]);
            }
        }

        if (min > 1) { // 1 is the smallest positive
            return 1;
        }

        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            if (num >= 0) {
                numSet.add(num); // fill the slots with a number
            }
        }

        for (int i = min; i <= max; i++) {
            if (!numSet.contains(i)) { // find the first missing slot which is the smallest positive
                return i;
            }
        }

        return max + 1;
    }

    public static void main(String[] args) {
        FirstMissingPositive f = new FirstMissingPositive();
        System.out.println(f.firstMissingPositive(new int[]{7,8,9,11,12}));
    }
}
