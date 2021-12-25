package Other;

import java.util.Arrays;

// https://leetcode.ca/2016-12-04-370-Range-Addition/
// similar with CorporateFlightBookings
public class RangeAddition {
    public int[] getModifiedArray(int length, int[][] updates) {
        int[] res = new int[length];
        int[] diff = new int[length];

        for (int[] update : updates) {
            int i = update[0];
            int j = update[1];
            int val = update[2];

            diff[i] += val;
            if (j + 1 < length) {
                diff[j + 1] -= val;
            }
        }

        res[0] = diff[0];
        for (int i = 1; i < length; i++) {
            res[i] = res[i - 1] + diff[i];
        }

        return res;
    }

    public static void main(String[] args) {
        int length = 5;
        int[][] updates = {
                {1, 3, 2},
                {2, 4, 3},
                {0, 2, -2}
        };

        RangeAddition r = new RangeAddition();
        System.out.println(Arrays.toString(r.getModifiedArray(length, updates)));
    }
}
