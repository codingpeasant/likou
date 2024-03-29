package SlidingWindow;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
public class BestTimeToBuySellStock {
    // https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
    // Same with MaxSubarray
    public int maxProfit(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur + (prices[i] - prices[i - 1]));
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }

    public int maxProfitState(int[] prices) {
        int hold = Integer.MIN_VALUE;
        int sold = 0;

        for (int price : prices) {
            hold = Math.max(hold, -price);
            sold = Math.max(sold, hold + price);
        }

        return sold;
    }

    public static void main(String[] args) {
        BestTimeToBuySellStock mdt = new BestTimeToBuySellStock();
        int[] sequence = {2,1,3,6,1,2,1,5,4};
        System.out.println("Max Profit: " + mdt.maxProfit(sequence));
        System.out.println("Max Profit: " + mdt.maxProfitState(sequence));
    }
}
