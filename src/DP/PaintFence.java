package DP;

public class PaintFence {
    public int numWays(int n, int k) {
        if (n == 1) {
            return k;
        }

        int same = k;
        int diff = k * (k - 1);

        for (int i = 3; i <= n; i++) {
            int sameTemp = same;
            same = diff;
            diff = (sameTemp + diff) * (k - 1);
        }

        return same + diff;
    }

    public int numWays2(int n, int k) {
        int[] dp = new int[n + 1];

        dp[1] = k;
        int same = 0, diff = k;

        for (int i = 2; i <= n; i++) {
            same = diff;
            diff = (dp[i - 1]) * (k - 1);
            dp[i] = same + diff;
        }

        return same + diff;
    }

    public static void main(String[] args) {
        PaintFence mdt = new PaintFence();
        System.out.println("Ways: " + mdt.numWays(4, 2));
        System.out.println("Ways2: " + mdt.numWays2(4, 2));
    }
}
