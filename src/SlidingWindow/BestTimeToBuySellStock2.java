package SlidingWindow;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
public class BestTimeToBuySellStock2 {
    // can sell and buy at the same day
    public int maxProfit(int[] prices) {
        int profit = 0;

        for (int i = 1; i < prices.length; i++)
            profit += Math.max(0, prices[i] - prices[i - 1]);

        return profit;
    }

    public static void main(String[] args) {
        BestTimeToBuySellStock2 mdt = new BestTimeToBuySellStock2();
        int[] sequence = {2,1,3,4,1,2,1,5,4};
        System.out.println("Max Profit: " + mdt.maxProfit(sequence));
    }
}
