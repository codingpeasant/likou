package Binary;

import java.util.Arrays;

// https://leetcode.com/problems/koko-eating-bananas/
public class KokoEatingBananas {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();
        // find the minimum speed using binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canEatAll(piles, h, mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left; // get the lower bound
    }

    private boolean canEatAll(int[] piles, int h, int k) {
        int hours = 0;
        for (int i = 0; i < piles.length; i++) {
            hours += piles[i] / k;
            if (piles[i] % k != 0) {
                hours++;
            }
        }
        return hours <= h;
    }

    public static void main(String[] args) {
        KokoEatingBananas k = new KokoEatingBananas();
        int[] piles = {3, 6, 7, 11};
        System.out.println(k.minEatingSpeed(piles, 8));
    }
}
