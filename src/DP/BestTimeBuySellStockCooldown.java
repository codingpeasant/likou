package DP;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
public class BestTimeBuySellStockCooldown {
    public int maxProfit(int[] prices) {
        int sold = 0, hold = Integer.MIN_VALUE, rest = 0;
        for (int i = 0; i < prices.length; ++i) {
            hold = Math.max(hold, rest - prices[i]); // need hold to be the first state, otherwise there won't be sold
            rest = Math.max(rest, sold);
            sold = Math.max(sold, hold + prices[i]);
        }
        return Math.max(sold, rest);
    }

    public static void main(String args[]) {
        int[] prices = new int[]{1, 2, 3, 0, 2};
        BestTimeBuySellStockCooldown b = new BestTimeBuySellStockCooldown();
        System.out.println(b.maxProfit(prices));
    }
}
