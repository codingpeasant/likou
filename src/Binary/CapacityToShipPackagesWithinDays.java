package Binary;

import java.util.Arrays;

// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
public class CapacityToShipPackagesWithinDays {
    public int shipWithinDays(int[] weights, int days) {
        int right = Arrays.stream(weights).sum();
        int left = Arrays.stream(weights).max().getAsInt();
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canShipAll(weights, days, mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean canShipAll(int[] weights, int days, int cap) {
        int daysTaken = 1;
        int currentWeight = 0;
        for (int i = 0; i < weights.length; i++) {
            if (currentWeight + weights[i] > cap) {
                daysTaken++;
                currentWeight = weights[i];
            } else {
                currentWeight += weights[i];
            }
        }
        return daysTaken <= days;
    }

    public static void main(String[] args) {
        CapacityToShipPackagesWithinDays c = new CapacityToShipPackagesWithinDays();
        int[] weights = {3, 2, 2, 4, 1, 4};
        System.out.println(c.shipWithinDays(weights, 3));
    }

}
