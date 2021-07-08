package Other;

public class Search2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowNum = matrix.length;
        int colNum = matrix[0].length;

        int left = 0;
        int right = rowNum * colNum - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int midValue = matrix[mid/colNum][mid%colNum];

            if (midValue == target) {
                return true;
            } else if (midValue < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }

    public static void main(String args[]) {
        Search2DMatrix s = new Search2DMatrix();
        int[][] input = {
                {1,   3,  5,  7},
                {10, 11, 16, 20},
                {23, 30, 34, 50}
        };

        System.out.println("exist: " + s.searchMatrix(input, 10));
    }
}
