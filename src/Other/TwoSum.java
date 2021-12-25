package Other;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/two-sum/
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> numIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int rest = target - nums[i];
            if (numIndex.containsKey(rest)) {
                res[0] = numIndex.get(rest);
                res[1] = i;
                return res;
            }
            numIndex.put(nums[i], i);
        }
        return res;
    }

    public static void main(String[] args) {
        TwoSum t = new TwoSum();
        int[] numts = {2, 7, 11, 15};
        System.out.println(Arrays.toString(t.twoSum(numts, 13)));
    }
}
