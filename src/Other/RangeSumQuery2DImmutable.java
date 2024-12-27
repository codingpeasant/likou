package Other;

// https://leetcode.com/problems/range-sum-query-2d-immutable/
public class RangeSumQuery2DImmutable {
    private int[][] preSum;

    public RangeSumQuery2DImmutable(int[][] matrix) {
        if (matrix == null
                || matrix.length == 0
                || matrix[0].length == 0) {
            return;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        preSum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int iMin = Math.min(row1, row2);
        int iMax = Math.max(row1, row2);

        int jMin = Math.min(col1, col2);
        int jMax = Math.max(col1, col2);

        return preSum[iMax + 1][jMax + 1] - preSum[iMax + 1][jMin] - preSum[iMin][jMax + 1] + preSum[iMin][jMin];
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {3,0,1},
                {5,6,3},
                {1,2,0}
        };

        RangeSumQuery2DImmutable r = new RangeSumQuery2DImmutable(matrix);
        System.out.println(r.sumRegion(1,1,2,2));
    }
}
