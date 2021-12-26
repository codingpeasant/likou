package Array;

import java.util.Arrays;

// https://leetcode.ca/2016-12-04-370-Range-Addition/
// similar with CorporateFlightBookings
public class RangeAddition {
    public int[] getModifiedArray(int length, int[][] updates) {

        int[] ans = new int[length];

        for (int[] update : updates) {
            int start = update[0];
            int end = update[1];
            int inc = update[2];

            ans[start] += inc;
            if (end + 1 < length) {
                ans[end + 1] -= inc;
            }

            System.out.println(Arrays.toString(ans));
//                [0, 0, 0, 0, 0]
//                [0, 2, 0, 0, -2]
//                [0, 2, 3, 0, -2]
//                [-2, 2, 3, 2, -2]
        }

        for (int i = 1; i < length; i++) {
            ans[i] += ans[i - 1]; // @note
        }
//                [-2, 0, 3, 5, 3]

        return ans;
    }

    public static void main(String[] args) {
        int length = 5;
        int[][] updates = {
                {1, 3, 2},
                {2, 4, 3},
                {0, 2, -2}
        };

        RangeAddition r = new RangeAddition();
        System.out.println("ANS: " + Arrays.toString(r.getModifiedArray(length, updates)));
    }
}
