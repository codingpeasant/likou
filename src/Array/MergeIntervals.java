package Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

// https://leetcode.com/problems/merge-intervals/
public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        Arrays.sort(intervals, Comparator.comparingInt(el -> el[0])); // (el1, el2) -> (el1[0] - el2[0])

        List<int[]> result = new ArrayList<>();
        int[] curInterval = intervals[0];
        result.add(curInterval);

        for (int[] interval: intervals) {
            if (curInterval[1] >= interval[0]) { // overlap, merge the 2 intervals
                curInterval[1] = Math.max(curInterval[1], interval[1]); // adjust the existing range in the result
            } else { // no overlap, directly add it
                curInterval = interval;
                result.add(curInterval);
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public int[][] merge1(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(el -> el[0])); // (el1, el2) -> (el1[0] - el2[0])
        List<int[]> result = new ArrayList<>();
        int[] toAdd = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            int[] cur = intervals[i];
            if (toAdd[1] < cur[0]) {
                result.add(toAdd);
                toAdd = cur;
            } else {
                toAdd[1] = Math.max(cur[1], toAdd[1]);
            }
        }
        result.add(toAdd);
        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        MergeIntervals m = new MergeIntervals();
        int[][] input = {{1,3}, {2,6}, {15,18}, {3, 5}};
        System.out.println("intervals after merge: " + Arrays.deepToString(m.merge(input)));
        System.out.println("intervals after merge: " + Arrays.deepToString(m.merge1(input)));
    }
}
