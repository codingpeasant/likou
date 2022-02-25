package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/remove-k-digits/
// when increasing, keep the smaller at the beginning; when decreasing, remove the larger at the beginning
public class RemoveKDigits {
    public String removeKDigits(String num, int k) {
        if (k == num.length()) return "0";

        int temp = k;
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < num.length(); i++) {
            while (k > 0 && !stack.isEmpty() && num.charAt(i) < stack.peek()) {
                stack.pop();
                k--;
            }
            stack.push(num.charAt(i));
        }

        // only get max k - temp elements
        StringBuilder sb = new StringBuilder();
        for (Character c : stack) {
            if (sb.length() < num.length() - temp)
                sb.append(c);
        }

        while (sb.length() > 1 && sb.charAt(0) == '0')
            sb.deleteCharAt(0);
        return sb.toString();
    }

    public static void main(String[] args) {
        RemoveKDigits r = new RemoveKDigits();
        int k = 3;
        String input = "1432219";
        System.out.println(r.removeKDigits(input, k));
    }
}
