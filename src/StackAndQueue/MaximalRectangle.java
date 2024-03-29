package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/maximal-rectangle/
// get histogram length and use largest-rectangle-in-histogram to calculate area
public class MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length <= 0) return 0;
        int n = matrix.length;
        int m = matrix[0].length;
        int[][] dp = new int[n][m];
        int maxArea = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0)
                    dp[i][j] = matrix[i][j] == '1' ? 1 : 0;
                else
                    dp[i][j] = matrix[i][j] == '1' ? (dp[i - 1][j] + 1) : 0;
//                int min = dp[i][j];
//                for (int k = j; k >= 0; k--) {
//                    if (min == 0) break;
//                    if (dp[i][k] < min) min = dp[i][k];
//                    maxArea = Math.max(maxArea, min * (j - k + 1));
//                }
            }
            maxArea = findCurrentMaxArea(dp[i], maxArea);
        }
        return maxArea;
    }

    private int findCurrentMaxArea(int[] heights, int maxArea) {
        int n = heights.length;
        Stack<Integer> indexStack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!indexStack.empty() && heights[i] < heights[indexStack.peek()]) {
                int curMax = heights[indexStack.pop()] * (i - (indexStack.isEmpty() ? 0 : indexStack.peek() + 1));
                maxArea = Math.max(curMax, maxArea);
            }
            indexStack.push(i);
        }

        while (!indexStack.isEmpty()) {
            int curMax = heights[indexStack.pop()] * (n - (indexStack.isEmpty() ? 0 : indexStack.peek() + 1));
            maxArea = Math.max(maxArea, curMax);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        MaximalRectangle m = new MaximalRectangle();
        char[][] matrix = {
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'},
        };
        System.out.println(m.maximalRectangle(matrix)); // 6
    }

}
