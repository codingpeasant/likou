package DP;

// https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226670/Java-DP-Solution-with-explanation-O(n)
// Similar with coin change
public class MinimumCostForTickets {
    public int mincostTickets(int[] days, int[] costs) {
        boolean[] daysExist = new boolean[366];
        for (int day : days) {
            daysExist[day] = true;
        }
        int[] minCostAtDay = new int[366]; // minCostAtDay[0] = 0;
        for (int i = 1; i <= 365; i++) {
            if (!daysExist[i]) {
                minCostAtDay[i] = minCostAtDay[i - 1]; // if this day doesn't exist
            } else {
                int min = minCostAtDay[i - 1] + costs[0]; // try to buy 1 day ticket
                min = Math.min(min, minCostAtDay[Math.max(i - 7, 0)] + costs[1]); // try to buy 7 day ticket at (i - 7)th day
                min = Math.min(min, minCostAtDay[Math.max(i - 30, 0)] + costs[2]); // try to buy 30 day ticket at (i - 30)th day
                minCostAtDay[i] = min;
            }
        }
        return minCostAtDay[365];
    }

    public static void main(String args[]) {
        int[] days = new int[]{1,4,6,7,8,20};
        int[] costs = new int[]{2,7,15};
        MinimumCostForTickets m = new MinimumCostForTickets();
        System.out.println(m.mincostTickets(days, costs));
    }

}
