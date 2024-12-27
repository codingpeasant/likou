package Binary;

import java.util.Arrays;

// https://leetcode.ca/2019-04-14-1231-Divide-Chocolate/
public class DivideChocolate {
    public int maximizeSweetness(int[] sweetness, int K) {
        int sum = Arrays.stream(sweetness).sum();
        int min = Arrays.stream(sweetness).min().getAsInt();

        if (K == 0)
            return sum;
        if (K + 1 > sweetness.length) {
            return 0;
        }

        int low = min, high = sum / (K + 1); // the max possible for my chocolate is the mean; suppose there is only 1 friend
        int max = 0;
        while (low <= high) {
            int mid = (high - low) / 2 + low;
            if (canDivide(sweetness, K + 1, mid)) {
                max = Math.max(max, mid);
                low = mid + 1;
            } else
                high = mid - 1;
        }
        return max;
    }

    public boolean canDivide(int[] sweetness, int chunks, int lowerBound) {
        int sum = 0;
        int count = 0;
        int length = sweetness.length;
        for (int i = 0; i < length; i++) {
            int num = sweetness[i];
            sum += num;
            if (sum >= lowerBound) {
                count++;
                if (count == chunks)
                    break;
                sum = 0;
            }
        }
        return count >= chunks;
    }
    public static void main(String[] args) {
        DivideChocolate d = new DivideChocolate();
        System.out.println(d.maximizeSweetness(new int[]{1,2,3,4,5,6,7,8,9}, 5));
    }
}
