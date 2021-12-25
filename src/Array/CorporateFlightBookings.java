package Array;

import java.util.Arrays;

// https://leetcode.com/problems/corporate-flight-bookings/
public class CorporateFlightBookings {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res = new int[n];
        int[] diff = new int[n];

        for (int i = 0; i < bookings.length; i++) {
            int first = bookings[i][0] - 1;
            int last = bookings[i][1] - 1;
            int val = bookings[i][2];

            diff[first] += val;
            if (last + 1 < n) {
                diff[last + 1] -= val;
            }
        }

        res[0] = diff[0];
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] + diff[i];
        }

        return res;
    }

    public int[] corpFlightBookings1(int[][] bookings, int n) {
        int[] res = new int[n];
        for (int[] b : bookings) {
            res[b[0] - 1] += b[2];
            if (b[1] < n) res[b[1]] -= b[2];
        }
        for (int i = 1; i < n; ++i)
            res[i] += res[i - 1];
        return res;
    }

    public static void main(String[] args) {
        int length = 5;
        int[][] updates = {
                {1, 2, 10},
                {2, 3, 20},
                {2, 5, 25}
        };

        CorporateFlightBookings c = new CorporateFlightBookings();
        System.out.println(Arrays.toString(c.corpFlightBookings(updates, length)));
        System.out.println(Arrays.toString(c.corpFlightBookings1(updates, length)));
    }
}
