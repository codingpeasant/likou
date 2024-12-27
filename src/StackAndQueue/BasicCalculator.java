package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/basic-calculator/
public class BasicCalculator {
    public int calculate(String s) {
        if (s == null) return 0;

        int result = 0;
        int sign = 1;
        int num = 0;

        Stack<Integer> stack = new Stack<>(); // the stack only has sign
        stack.push(sign);

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '+' || c == '-') { // clear the previous result before sign change
                result += sign * num;
                System.out.println(result + " " + sign);
                sign = stack.peek() * (c == '+' ? 1 : -1); // check the previous sign to generate the current -- is +; +- is -; ++ is +
                num = 0;
            } else if (c == '(') { // stack to track the previous sign before the (
                stack.push(sign);
            } else if (c == ')') {
                stack.pop();
            }
        }

        result += sign * num;
        return result;
    }

    public static void main(String[] args) {
        BasicCalculator b = new BasicCalculator();
        System.out.println(b.calculate("10+15-(10-(4+5)-3)+1")); // calculate() is converting it to 10+15-10+4+5+3+1
    }
}
