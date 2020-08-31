package Stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        String input = "[]{}";
        ValidParentheses v = new ValidParentheses();
        System.out.println("Is valid: " + v.isValid(input));
    }
}
