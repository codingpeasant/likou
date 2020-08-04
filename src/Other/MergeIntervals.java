package Other;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        Arrays.sort(intervals, Comparator.comparingInt(el -> el[0])); // (el1, el2) -> (el1[0] - el2[0])

        List<int[]> result = new ArrayList<>();
        int[] curInterval = intervals[0];
        result.add(curInterval);

        for (int[] interval: intervals) {
            if (curInterval[1] > interval[0]) {
                curInterval[1] = Math.max(curInterval[1], interval[1]); // adjust the existing range in the result
            } else {
                curInterval = interval;
                result.add(curInterval);
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        MergeIntervals m = new MergeIntervals();
        int[][] input = {{1,3}, {2,6}, {15,18}, {3, 5}};
        System.out.println("intervals after merge: " + Arrays.deepToString(m.merge(input)));
    }
}
