package DP;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

// https://leetcode.com/problems/coin-change/
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
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1); // based on the previous min + 1
                }
            }
        }

        if (dp[amount] == Integer.MAX_VALUE - 1) {
            return -1;
        }
        return dp[amount];
    }

    public int coinChangeRecursive(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        if (amount < 0) {
            return -1;
        }

        int res = Integer.MAX_VALUE;
        for (int coin:coins) {
            int subProblem = coinChangeRecursive(coins, amount - coin);
            if (subProblem == -1) continue;
            res = Math.min(res, subProblem + 1);
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }

    // exhaust all possibilities and find the min
    int min = Integer.MAX_VALUE;
    public void backtrack(int[] nums, int amount, List<Integer> currentList, int curSum, int start) {
        if (curSum == amount) {
            min = Math.min(min, currentList.size());
            currentList.forEach(item -> System.out.print(item + ","));
            System.out.println("[" + min + "]");
            return;
        }

        if (curSum > amount) {
            return;
        }

        for (int i = start; i < nums.length; i++) {
            curSum += nums[i];
            currentList.add(nums[i]);
            backtrack(nums, amount, currentList, curSum, i);
            currentList.remove(currentList.size() - 1);
            curSum -= nums[i];
        }
    }

    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int value = 6;
        CoinChange v = new CoinChange();
        v.backtrack(coins, value, new ArrayList<Integer>(), 0, 0);
        System.out.println("Min coins: " + v.coinChange(coins, value));
        System.out.println("Min coins (recursive): " + v.coinChangeRecursive(coins, value));
//
//        ArrayList<Integer> movies = new ArrayList<>();
//        movies.add(1);
//        movies.add(3);
//        movies.add(2);
//        movies.sort((o1, o2) -> o2 - o1);
//        for (int movie: movies
//             ) {
//            System.out.println(movie);
//        }
//
//        PriorityQueue<Integer> pairs = new PriorityQueue<>((o1, o2) -> o2 - o1);
//        pairs.add(1);
//        pairs.add(3);
//        pairs.add(2);
//        System.out.println(pairs.remove());
    }
}