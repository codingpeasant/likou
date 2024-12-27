package Array;

import javax.sound.midi.SysexMessage;
import java.util.Arrays;

// https://leetcode.com/problems/remove-covered-intervals/
public class RemoveCoveredIntervals {
    public int removeCoveredIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        int res = 1;
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]); // suppose a could possibly cover b
        int preRight = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][1] > preRight) {
                res++;
                preRight = intervals[i][1];
            }
        }

        return res;
    }

    public static void main(String[] args) {
        RemoveCoveredIntervals r = new RemoveCoveredIntervals();
        int[][] input = {
                {1, 4},
                {3, 6},
                {2, 8}
        };
        System.out.println(r.removeCoveredIntervals(input));
    }
}
