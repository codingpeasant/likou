package Other;

import java.util.Arrays;

// https://leetcode.com/problems/maximum-units-on-a-truck/
// Greedy
public class MaximumUnitsTruck {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        int res = 0;

        for (int i = 0; i < boxTypes.length && truckSize > 0; i++) {
            int min = Math.min(truckSize, boxTypes[i][0]);
            truckSize -= min;
            res += min * boxTypes[i][1];
        }

        return res;
    }

    public static void main(String[] args) {
        MaximumUnitsTruck m = new MaximumUnitsTruck();
        System.out.println(m.maximumUnits(new int[][]{{1,3},{2,2},{3,1}}, 4));
    }
}
