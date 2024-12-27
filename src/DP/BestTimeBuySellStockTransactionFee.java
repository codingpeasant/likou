package DP;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
public class BestTimeBuySellStockTransactionFee {
    public int maxProfit(int[] prices, int fee) {
        int hold = Integer.MIN_VALUE; // need hold to be the first state, otherwise there won't be sold
        int sold = 0;

        for (int price : prices) {
            hold = Math.max(hold, sold - price);
            sold = Math.max(sold, hold + price - fee);
        }

        return sold;
    }

    public static void main(String[] args) {
        BestTimeBuySellStockTransactionFee b = new BestTimeBuySellStockTransactionFee();
        int[] prices = {1,3,7,5,10,3};
        int fee = 3;
        System.out.println(b.maxProfit(prices, fee));
    }
}
