package Other;

import java.util.Arrays;
import java.util.PriorityQueue;

public class MeetingRoom2 {
    public class Interval {
        int start;
        int end;

        Interval() {
            start = 0;
            end = 0;
        }

        Interval(int s, int e) {
            start = s;
            end = e;
        }
    }

    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, (a, b) -> a.start - b.start); // make sure current.start >= earliestEnd.end works
        PriorityQueue<Interval> endTimeHeap = new PriorityQueue<>((a, b) -> a.end - b.end);
        endTimeHeap.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            Interval current = intervals[i];
            Interval earliestEnd = endTimeHeap.poll();
            if (current.start >= earliestEnd.end) {
                earliestEnd.end = current.end;
            } else {
                endTimeHeap.add(current);
            }
            endTimeHeap.add(earliestEnd);
        }
        return endTimeHeap.size();
    }

    public void initialize() {
        Interval[] intervals = new Interval[3];
        intervals[0] = new Interval(0, 30);
        intervals[2] = new Interval(5, 10);
        intervals[1] = new Interval(15, 20);

        System.out.println("number of rooms: "+minMeetingRooms(intervals));
    }

    public static void main(String[] args) {
        MeetingRoom2 m = new MeetingRoom2();
        m.initialize();
    }

}
