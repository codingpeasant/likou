package BackTrack;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(candidates, target, list, new ArrayList<Integer>(), 0, 0);
        return list;
    }

    public void backtrack(int[] candidate, int target, List<List<Integer>> list, List<Integer> curList, int curSum, int start) {
        if (curSum == target) {
            list.add(new ArrayList<>(curList));
        }

        if (curSum > target) {
            return;
        }

        for (int i = start; i < candidate.length; i++) {
            curSum += candidate[i];
            curList.add(candidate[i]);
            backtrack(candidate, target, list, curList, curSum, i);
            curSum -= candidate[i];
            curList.remove(curList.size() - 1);
        }
    }

    public static void main(String[] args) {
        CombinationSum c = new CombinationSum();
        int[] input = {10,1,2,7,6,5};
        System.out.println("All combinations: " + c.combinationSum(input, 8));
    }
}
