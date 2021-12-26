package Array;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.TreeMap;

// https://leetcode.ca/2016-08-09-253-Meeting-Rooms-II/
// similar with CorporateFlightBookings, CarPooling
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

    public int minMeetingRooms2(Interval[] intervals) {
        TreeMap<Integer, Integer> m = new TreeMap<>();

        for (Interval each: intervals) {
            int start = each.start;
            int end = each.end;
            m.put(start, 1 + m.getOrDefault(start, 0));
            m.put(end, m.getOrDefault(end, 0) - 1);
        }

        int active = 0;
        int result = 0;

        // If a time is the end time of one meeting and the start time of another meeting,
        // the mapping value is decreased first and then increased and remains at 0, no new room is allocated
        for (int v: m.values()) {
            active += v;
            result = Math.max(result, active);
        }

        return result;
    }

    public void initialize() {
        Interval[] intervals = new Interval[3];
        intervals[0] = new Interval(0, 30);
        intervals[2] = new Interval(5, 10);
        intervals[1] = new Interval(15, 20);

        //System.out.println("number of rooms: "+minMeetingRooms(intervals));
        System.out.println("number of rooms: "+minMeetingRooms2(intervals));
    }

    public static void main(String[] args) {
        MeetingRoom2 m = new MeetingRoom2();
        m.initialize();
    }

}
