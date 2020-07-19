package Other;

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();

        if (matrix.length == 0){
            return res;
        }

        int rowBegin = 0;
        int rowEnd = matrix.length - 1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;

        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            // Right
            for (int i = colBegin; i <= colEnd; i++) {
                res.add(matrix[rowBegin][i]);
            }
            rowBegin++;

            // Down
            for (int i = rowBegin; i <= rowEnd; i++) {
                res.add(matrix[i][colEnd]);
            }
            colEnd--;

            // Left
            for (int j = colEnd; j >= colBegin; j --) {
                res.add(matrix[rowEnd][j]);
            }
            rowEnd--;

            // Up
            for (int j = rowEnd; j >= rowBegin; j --) {
                res.add(matrix[j][colBegin]);
            }
            colBegin++;
        }

        return res;
    }

    public static void main(String[] args) {
        int M[][] = new int[][]{
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };

        SpiralMatrix w = new SpiralMatrix();
        System.out.println("Spiral path: " + w.spiralOrder(M));
    }
}
