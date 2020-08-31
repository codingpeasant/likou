package Other;

import java.util.Arrays;
import java.util.Comparator;

// Greedy
public class NonOverlappingIntervals {
    static class Interval {
        int start;
        int end;

        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public int eraseOverlapIntervals(Interval[] intervals) {
        if (intervals.length == 0)  return 0;

        Arrays.sort(intervals, Comparator.comparingInt(a -> a.end));

        int end = intervals[0].end;
        int count = 1;

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i].start >= end) {
                end = intervals[i].end;
                count++;
            }
        }

        return intervals.length - count;
    }

    public static void main(String[] args) {
        NonOverlappingIntervals non = new NonOverlappingIntervals();
        Interval[] intervals = new Interval[]{
                new Interval(1,2),
                new Interval(2,3),
                new Interval(3,4),
                new Interval(1,3),
        };

        System.out.println(non.eraseOverlapIntervals(intervals));
    }
}
