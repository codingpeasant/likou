package DP;

import java.util.Arrays;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
public class BestTimeBuySellStock4 {
    // Time complexity: O(kn) where k is k, n is the number of prices
    // Space complexity: O(kn)
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (k >= n/2) {
            // fast case because there are [0, n/2] continuous increases
            int maxProfit = 0;
            for (int i = 1; i < n; i++) {
                int diff = prices[i] - prices[i-1];
                if (diff > 0) {
                    maxProfit += diff;
                }
            }
            return maxProfit;
        }

        // sell is all 0 (don't buy or sell at all); hold should be maximized
        int[] hold = new int[k + 1], sell = new int[k + 1];
        Arrays.fill(hold, Integer.MIN_VALUE);
        for (int price : prices) {
            for (int i = 1; i <= k; i++) {
                hold[i] = Math.max(hold[i], sell[i - 1] - price); // either stay at the same state or transfer from previous sold state by buying at the current price
                sell[i] = Math.max(sell[i], hold[i] + price); // either stay at the same state or transfer from current hold by selling at the current price
            }
        }
        return sell[k];
    }

    public static void main(String[] args) {
        BestTimeBuySellStock4 b = new BestTimeBuySellStock4();
        System.out.println(b.maxProfit(2, new int[]{3,2,6,5,0,3}));
    }
}
