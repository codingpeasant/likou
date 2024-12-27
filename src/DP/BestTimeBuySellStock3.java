package DP;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
public class BestTimeBuySellStock3 {
    public int maxProfit(int[] prices) {
        int oneBuy = Integer.MAX_VALUE;
        int twoBuy = Integer.MAX_VALUE;
        int oneSell = 0; // worst case: never buy or sell
        int twoSell = 0;

        for (int price : prices) {
            oneBuy = Math.min(oneBuy, price); // find the min to make the first buy
            oneSell = Math.max(oneSell, price - oneBuy); // max the profit if sell here
            twoBuy = Math.min(twoBuy, price - oneSell); // find the min to make the second buy after selling the first
            twoSell = Math.max(twoSell, price - twoBuy); // max the profit if sell here the second time - worst case twoSell == oneSell
        }

        // so return twoSell
        return twoSell;
    }

    // state machine
    public int maxProfit1(int[] prices) {
        int hold1 = Integer.MIN_VALUE; // needs to find max first state
        int hold2 = Integer.MIN_VALUE; // needs to find the max hold price
        int sold1 = 0; // worst case: never buy or sell
        int sold2 = 0;

        for (int price : prices) {
            hold1 = Math.max(hold1, -price); // either stay at the same state or buying at the current price
            sold1 = Math.max(sold1, hold1 + price); // either stay at the same state or transfer from hold1 by selling at the current price
            hold2 = Math.max(hold2, sold1 - price); // either stay at the same state or transfer from sold1 by buying at the current price
            sold2 = Math.max(sold2, hold2 + price); // either stay at the same state or transfer from hold2 by selling at the current price
        }

        return sold2;
    }

    public static void main(String[] args) {
        BestTimeBuySellStock3 b = new BestTimeBuySellStock3();
        int[] prices = new int[]{3, 3, 5, 0, 0, 3, 1, 4};
        System.out.println(b.maxProfit(prices));
        System.out.println(b.maxProfit1(prices));
    }
}
