package Other;

// https://leetcode.com/problems/car-pooling/
public class CarPooling {
    public boolean carPooling(int[][] trips, int capacity) {
        int stops[] = new int[1001];
        for (int t[] : trips) {
            stops[t[1]] += t[0];
            stops[t[2]] -= t[0];
        }
        for (int i = 0; capacity >= 0 && i < 1001; ++i) capacity -= stops[i];
        return capacity >= 0;
    }

    // or similar with CorporateFlightBookings
    public boolean carPooling2(int[][] trips, int capacity) {
        int[] diff = new int[1000];
        int[] people = new int[1000];

        for (int[] trip:trips) {
            int num = trip[0];
            int start = trip[1];
            int end = trip[2];

            diff[start] += num;
            if (end < 999) {
                diff[end] -= num;
            }
        }

        people[0] = diff[0];
        if (people[0] > capacity) return false;
        for (int i = 1; i < 1000; i++) {
            people[i] = people[i - 1] + diff[i];
            if (people[i] > capacity) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        int cap = 10;
        CarPooling c = new CarPooling();
        int[][] updates = {
                {9, 0, 1},
                {3, 3, 7}
        };
        System.out.println(c.carPooling(updates, cap));
        System.out.println(c.carPooling2(updates, cap));
    }
}
