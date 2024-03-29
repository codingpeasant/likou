package Array;

import java.util.*;

// https://leetcode.com/problems/insert-interval/
public class InsertInterval {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<>();
        int[] toAdd = newInterval;

        for (int i = 0; i < intervals.length; i ++) {
            /*1. No overlap and toAdd appears before current interval, add toAdd to result.*/
            if (intervals[i][0] > toAdd[1]) {
                ans.add(toAdd);
                toAdd = intervals[i];
            }
            /*2. Has overlap, update the toAdd to the merged interval.*/
            else if (intervals[i][1] >= toAdd[0])
                toAdd = new int[] {Math.min(intervals[i][0], toAdd[0]),
                        Math.max(intervals[i][1], toAdd[1]) };
            /*3. No overlap and toAdd appears after current interval, add current interval to result.*/
            else ans.add(intervals[i]);
        }
        ans.add(toAdd);
        int[][] arrayAns = new int[ans.size()][2];
        return ans.toArray(arrayAns);
    }

    public static void main(String[] args) {
        InsertInterval i = new InsertInterval();
        int[][] intervals = {
                {1,3},
                {6,9}
        };
        int[] newInterval = {2,5};
        System.out.println(Arrays.deepToString(i.insert(intervals, newInterval)));
    }
}
