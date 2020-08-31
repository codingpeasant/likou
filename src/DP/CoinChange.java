package DP;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE - 1);

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

        if (dp[amount] == Integer.MAX_VALUE - 1) {
            return -1;
        }
        return dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = {10, 5, 7};
        int value = 11;
        CoinChange v = new CoinChange();
        System.out.println("Min coins: " + v.coinChange(coins, value));

        ArrayList<Integer> movies = new ArrayList<>();
        movies.add(1);
        movies.add(3);
        movies.add(2);
        movies.sort((o1, o2) -> o2 - o1);
        for (int movie: movies
             ) {
            System.out.println(movie);
        }

        PriorityQueue<Integer> pairs = new PriorityQueue<>((o1, o2) -> o2 - o1);
        pairs.add(1);
        pairs.add(3);
        pairs.add(2);
        System.out.println(pairs.remove());
    }
}