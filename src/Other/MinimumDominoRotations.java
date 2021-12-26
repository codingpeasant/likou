package Other;

// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
public class MinimumDominoRotations {
    public int minDominoRotations(int[] A, int[] B) {
        int[] countA = new int[7], countB = new int[7], same = new int[7];
        int n = A.length;
        for (int i = 0; i < n; ++i) {
            countA[A[i]]++;
            countB[B[i]]++;
            if (A[i] == B[i])
                same[A[i]]++;
        }
        for (int i = 1; i < 7; ++i)
            if (countA[i] + countB[i] - same[i] == n)
                return n - Math.max(countA[i], countB[i]); // either first row or the second
        return -1;
    }

    public static void main(String[] args) {
        MinimumDominoRotations m = new MinimumDominoRotations();
        int[] A = {2, 2, 2, 4, 2, 2};
        int[] B = {5, 2, 6, 2, 3, 2};
        System.out.println("Min rotation: " + m.minDominoRotations(A, B));
    }
}
