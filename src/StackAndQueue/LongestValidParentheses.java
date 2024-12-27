package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/longest-valid-parentheses/
public class LongestValidParentheses {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        int max = 0;
        int left = -1; // when (), j = 1, left = -1 and max = 1 - (-1) = 2
        for (int j = 0; j < s.length(); j++) {
            if (s.charAt(j) == '(') stack.push(j);
            else {
                if (stack.isEmpty()) // nothing in the stack to match ), so move left to the current invalid position
                    left = j;
                else {
                    stack.pop();
                    if (stack.isEmpty()) // all pairs since left were matched, directly j - left
                        max = Math.max(max, j - left);
                    else // some ( in the stack didn't match, go from the last ( in the stack
                        max = Math.max(max, j - stack.peek());
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        LongestValidParentheses l = new LongestValidParentheses();
        System.out.println(l.longestValidParentheses(")()())"));
    }
}
