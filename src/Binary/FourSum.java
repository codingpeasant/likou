package Binary;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/4sum/
public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new LinkedList<>();
        if (nums.length < 4) return res;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip the same result
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue; // skip the same result
                int lo = j + 1, hi = nums.length - 1, sum = target - nums[i] - nums[j];
                while (lo < hi) {
                    if (nums[lo] + nums[hi] == sum) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[lo], nums[hi]));
                        while (lo < hi && nums[lo] == nums[lo + 1]) lo++; // skip same result
                        while (lo < hi && nums[hi] == nums[hi - 1]) hi--;
                        lo++;
                        hi--;
                    } else if (nums[lo] + nums[hi] < sum) lo++;
                    else hi--;
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        FourSum fourSum = new FourSum();
        int[] input = {-3, -1, 0, 2, 4, 5};
        System.out.println(fourSum.fourSum(input, 0));
    }
}
