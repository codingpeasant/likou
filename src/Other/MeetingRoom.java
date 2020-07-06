package Other;

import java.util.Arrays;

public class MeetingRoom {
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

    public boolean canAttendMeetings(Interval[] intervals) {
        Arrays.sort(intervals, (a, b) -> a.start - b.start);
        for (int i = 1; i < intervals.length; i ++) {
            if (intervals[i].start < intervals[i-1].end) {
                return false;
            }
        }
        return true;
    }

    public void initialize() {
        Interval[] intervals = new Interval[3];
        intervals[0] = new Interval(0, 30);
        intervals[2] = new Interval(5, 10);
        intervals[1] = new Interval(15, 20);

        System.out.println("can attend all: "+canAttendMeetings(intervals));
    }

    public static void main(String[] args) {
        MeetingRoom m = new MeetingRoom();
        m.initialize();
    }
}
