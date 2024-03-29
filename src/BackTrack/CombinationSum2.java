package BackTrack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://leetcode.com/problems/combination-sum-ii/
public class CombinationSum2 {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates); // sort to skip the consecutive duplicate candidate
        List<List<Integer>> res = new ArrayList<>();
        dfs(candidates, target, new ArrayList<>(), res, 0, 0);
        return res;
    }

    private void dfs(int[] candidates, int target, List<Integer> curList, List<List<Integer>> res, int curSum, int start) {
        if (target == curSum) {
            res.add(new ArrayList<>(curList));
            return;
        }

        if (curSum > target) return;
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            curList.add(candidates[i]);
            curSum += candidates[i];
            dfs(candidates, target, curList, res, curSum, i + 1); // i + 1 guarantees that the next stack level doesn't pick the current candidate
            curList.remove(curList.size() - 1);
            curSum -= candidates[i];
        }
    }

    public static void main(String[] args) {
        CombinationSum2 c = new CombinationSum2();
        int[] input = {10, 1, 2, 7, 6, 1, 5};
        System.out.println("All combinations: " + c.combinationSum2(input, 8));
    }
}
