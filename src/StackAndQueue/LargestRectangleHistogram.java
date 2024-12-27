package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/largest-rectangle-in-histogram/
public class LargestRectangleHistogram {
    // 说的简单一点就是对于每一个柱子，找到左边的比它短的i, 右边比他短的j，然后局部max就是(j - i - 1) * h
    // the stack stores increasing height only, when seeing a shorter one, pop all the larger ones in the stack
    public int largestRectangleArea(int[] heights) {
        if (heights.length == 0) return 0;
        Stack<Integer> indexStack = new Stack<>();
        int len = heights.length;
        int maxArea = Integer.MIN_VALUE;

        for (int i = 0; i < len; i++) {
            while (!indexStack.isEmpty() && heights[i] < heights[indexStack.peek()]) {
                int curMax = heights[indexStack.pop()] * (i - (indexStack.isEmpty() ? 0 : indexStack.peek() + 1));
                maxArea = Math.max(maxArea, curMax);
            }
            indexStack.push(i);
        }

        while (!indexStack.isEmpty()) {
            int curMax = heights[indexStack.pop()] * (len - (indexStack.isEmpty() ? 0 : indexStack.peek() + 1));
            maxArea = Math.max(maxArea, curMax);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        LargestRectangleHistogram l = new LargestRectangleHistogram();
        int[] input = {2,1,5,6,2,3};
        System.out.println(l.largestRectangleArea(input));
    }

}
