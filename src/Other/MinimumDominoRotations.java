package Other;

public class MinimumDominoRotations {
    public int minDominoRotations(int[] A, int[] B) {
        if (A.length == 0 || B.length == 0) {
            return -1;
        }

        // don't flip first domino
        int notRotationFirst = Math.min(getRotations(A, B, A[0], true), getRotations(A, B, B[0], false));
        // flip first domino
        int rotationFirst = Math.min(getRotations(A, B, B[0], true) + 1, getRotations(A, B, A[0], false) + 1);
        if (notRotationFirst == Integer.MAX_VALUE - 1 || rotationFirst == Integer.MAX_VALUE) return -1;
        return Math.min(notRotationFirst, rotationFirst);
    }

    private int getRotations(int[] A, int[] B, int value, boolean isA) {
        int rotation = 0;
        for (int i = 1; i < A.length; i++) {
            if (isA) {
                if (A[i] == value) {
                    continue;
                }

                if (B[i] == value) {
                    rotation++;
                } else {
                    return Integer.MAX_VALUE - 1;
                }
            } else {
                if (B[i] == value) {
                    continue;
                }

                if (A[i] == value) {
                    rotation++;
                } else {
                    return Integer.MAX_VALUE - 1;
                }
            }
        }
        return rotation;
    }

    public static void main(String[] args) {
        MinimumDominoRotations m = new MinimumDominoRotations();
        int[] A = {2,2,2,4,2,2};
        int[] B = {5,2,6,2,3,2};
        System.out.println("Min rotation: " + m.minDominoRotations(A, B));
    }
}
