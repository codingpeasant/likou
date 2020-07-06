package DP;

import java.util.Arrays;

public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (i == coins[j]) {
                    dp[i] = 1;
                }

                if (i - coins[j] > 0) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }

        if (dp[amount] == Integer.MAX_VALUE) {
            return -1;
        }
        return dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = {1,2,5,7,10};
        int value = 11;
        CoinChange v = new CoinChange();
        System.out.println("Min coins: " + v.coinChange(coins, value));
    }
}