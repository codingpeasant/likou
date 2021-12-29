package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/basic-calculator-ii/
public class BasicCalculator2 {
    public int calculate(String s) {
        if (s == null || s.isEmpty()) return 0;

        int len = s.length();
        Stack<Integer> stack = new Stack<>(); // the stack only has number
        int currentNumber = 0;
        char operation = '+';

        for (int i = 0; i < len; i++) {
            char currentChar = s.charAt(i);
            if (Character.isDigit(currentChar)) {
                currentNumber = (currentNumber * 10) + (currentChar - '0');
            }
            if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == len - 1) {
                // Addition (+) or Subtraction (-): We must evaluate the expression later based on the next operation.
                // So, we must store the currentNumber to be used later. Let's push the currentNumber in the Stack.
                if (operation == '-') {
                    stack.push(-currentNumber);
                }
                else if (operation == '+') {
                    stack.push(currentNumber);
                }
                else if (operation == '*') {
                    stack.push(stack.pop() * currentNumber);
                }
                else if (operation == '/') {
                    stack.push(stack.pop() / currentNumber);
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }
        int result = 0;
        while (!stack.isEmpty()) { // all should be +
            result += stack.pop();
        }
        return result;
    }

    public static void main(String[] args) {
        BasicCalculator2 b = new BasicCalculator2();
        System.out.println(b.calculate("-22 - 3 * 5"));
    }
}
