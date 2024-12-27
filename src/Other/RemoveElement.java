package Other;

import java.util.Arrays;

// https://leetcode.com/problems/remove-element/
public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int slow = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[slow++] = nums[i];
            }
        }

        return slow;
    }

    public static void main(String[] args) {
        int[] nums = {0,1,2,2,3,0,4,2};
        RemoveElement r = new RemoveElement();
        System.out.println(r.removeElement(nums,2));
        System.out.println(Arrays.toString(nums));
    }
}
