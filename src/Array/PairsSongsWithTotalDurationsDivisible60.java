package Array;

// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
public class PairsSongsWithTotalDurationsDivisible60 {
    public int numPairsDivisibleBy60(int[] time) {
        int c[] = new int[60], res = 0;
        for (int t : time) {
            res += c[(60 - t % 60) % 60]; // (t + x) % 60 = 0 -> x % 60 = 60 - t % 60
            c[t % 60] += 1;
        }
        return res;
    }

    public static void main(String[] args) {
        PairsSongsWithTotalDurationsDivisible60 p = new PairsSongsWithTotalDurationsDivisible60();
        p.numPairsDivisibleBy60(new int[]{30,20,150,100,40});
    }
}
