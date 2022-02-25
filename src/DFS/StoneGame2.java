package DFS;

// https://leetcode.com/problems/stone-game-ii/
public class StoneGame2 {
    public int stoneGameII(int[] piles) {
        if (piles == null || piles.length == 0) return 0;

        // cache[i][j] is the max number of stones a player can get when the first pile is piles[i] and M == j.
        int[][] cache = new int[piles.length][piles.length];

        int[] suffixSum = new int[piles.length];    // suffixSum[i] starting from i sum up everything to the right: sum(piles[i, piles.length - 1])
        suffixSum[suffixSum.length - 1] = piles[piles.length - 1];
        for (int i = piles.length - 2; i >= 0; --i) suffixSum[i] = piles[i] + suffixSum[i + 1];

        return helper(piles, suffixSum, cache, 0, 1);
    }

    // dfs with memoization
    private int helper(int[] piles, int[] suffixSum, int[][] cache, int firstPile, int M) {
        if (firstPile == piles.length) return 0;    // no more piles left
        // Number of remaining piles is <= than the number of piles we can take in the current turn 2*M. We just take all remaining piles.
        if (piles.length - firstPile <= 2 * M) return suffixSum[firstPile];
        if (cache[firstPile][M] != 0) return cache[firstPile][M];

        int result = 0;
        // Try out all possible next moves, store the max amount of stones we can get
        for (int x = 1; x <= 2 * M; ++x) {
            // suffixSum[firstPile] is the total number of stones left in the game, it's the maximum possible gain.
            // helper(...) is the max amount of stones the next player can get if we make the current move x.
            // We want to make the move that minimizes the final gain of the next player, this move maximizes our own final gain.
            result = Math.max(result, suffixSum[firstPile] - helper(piles, suffixSum, cache, firstPile + x, Math.max(M, x)));
        }

        cache[firstPile][M] = result;
        return result;
    }

    public static void main(String[] args) {
        StoneGame2 s = new StoneGame2();
        int[] piles = {2, 7, 9, 4, 4};
        System.out.println(s.stoneGameII(piles));
    }

}
