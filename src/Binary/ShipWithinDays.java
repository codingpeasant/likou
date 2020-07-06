package Binary;

public class ShipWithinDays {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0, right = 0;
        for (int w: weights) {
            left = Math.max(left, w);
            right += w;
        }
        while (left < right) {
            int mid = (left + right) / 2, need = 1, cur = 0;
            for (int w: weights) {
                if (cur + w > mid) {
                    need += 1;
                    cur = 0;
                }
                cur += w;
            }
            if (need > D) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    public static void main(String[] args) {
        ShipWithinDays s = new ShipWithinDays();
        int[] input = {3,2,2,4,1,4};
        System.out.println("Min Cpa is: " + s.shipWithinDays(input, 3));
    }
}
