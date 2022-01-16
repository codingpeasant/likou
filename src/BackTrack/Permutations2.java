package BackTrack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://leetcode.com/problems/permutations-ii/
public class Permutations2 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        boolean[] used = new boolean[nums.length];
        List<Integer> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(nums, used, list, res);
        return res;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> curList, List<List<Integer>> res) {
        if (curList.size() == nums.length) {
            res.add(new ArrayList<>(curList));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            // we can make sure that 1b cannot be chosen before 1a; when a number has the same value with its previous,
            // we can use this number only if his previous is used
            // why used[] is needed while combinationSum2 doesn't? the latter doesn't need to start from 0,
            // no concern of picking a previous element or not
            if (i > 0 && nums[i - 1] == nums[i] && !used[i - 1]) continue;
            used[i] = true;
            curList.add(nums[i]);
            backtrack(nums, used, curList, res);
            used[i] = false;
            curList.remove(curList.size() - 1);
        }
    }

    public static void main(String[] args) {
        Permutations2 p = new Permutations2();
        int[] input = {1, 1, 2};
        System.out.println("All permutations: " + p.permuteUnique(input));
    }
}
