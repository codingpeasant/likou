package BackTrack;

import java.util.*;

// https://leetcode.com/problems/remove-invalid-parentheses/
public class RemoveInvalidParentheses {
    public List<String> removeInvalidParentheses(String s) {
        int left = 0, right = 0, count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else if (s.charAt(i) == ')') {
                if (left > 0)
                    left--;
                else
                    right++;
            }
        }
        // Find how many min. no. of changes are required
        count = left + right;
        Set<String> res = new HashSet<>();
        dfs(s, 0, res, new StringBuilder(), count);
        return new ArrayList<>(res);
    }

    boolean isValid(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') count++;
            if (c == ')' && count-- == 0) return false;
        }

        return count == 0;
    }

    boolean isValid2(String s) {
        Stack<Character> parenStack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') parenStack.add(')');
            else if (c == ')') {
                if (parenStack.isEmpty() || parenStack.pop() != c) {
                    return false;
                }
            }
        }
        return parenStack.isEmpty();
    }

    public void dfs(String s, int i, Set<String> res, StringBuilder sb, int count) {
        // draw a decision tree to understand it :)
        if (count < 0) {
            return;
        }
        if (i == s.length()) {
            if (count == 0) {
                if (isValid2(sb.toString())) {
                    res.add(sb.toString());
                }
            }
            return;
        }

        char c = s.charAt(i);
        int len = sb.length();

        if (c == '(' || c == ')') {
            dfs(s, i + 1, res, sb, count - 1);		    // not use ')''(', remove it, so count could be down
        }
        dfs(s, i + 1, res, sb.append(c), count);       // use

        sb.setLength(len);
    }

    public static void main(String[] args) {
        RemoveInvalidParentheses r = new RemoveInvalidParentheses();
        String input = "(a)())()";
        System.out.println(r.removeInvalidParentheses(input));
    }
}
