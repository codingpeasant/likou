package BackTrack;

import java.util.ArrayList;
import java.util.List;
// https://leetcode.com/problems/subsets/
public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(nums, list, new ArrayList<>(), 0);
        return list;
    }

    public void backtrack(int[] num, List<List<Integer>> list, List<Integer> curList, int start) {
        list.add(new ArrayList<>(curList));
        for (int i = start; i < num.length; i++) {
            curList.add(num[i]);
            backtrack(num, list, curList, i + 1);
            curList.remove(curList.size() - 1);
        }
    }

//      1     2      3
//    / | \  / \     |
//    _ 2  3 -  3    -
//    /  \
//    -   3
    public static void main(String[] args) {
        Subsets s = new Subsets();
        int[] input = {1,2,3};
        System.out.println("Subsets: " + s.subsets(input));
    }
}
