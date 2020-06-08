package Stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        if (s.isEmpty()) {
            return true;
        }

        Map<Character, Character> charMap = new HashMap<>();
        charMap.put(']', '[');
        charMap.put('}', '{');
        charMap.put(')', '(');

        Stack<Character> charStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (charMap.containsValue(cur)) {
                charStack.push(cur);
            } else {
                if (charStack.isEmpty()) {
                    return false;
                }
                Character topElem = charStack.pop();
                if (!topElem.equals(charMap.get(cur))) {
                    return false;
                }
            }
        }

        return charStack.isEmpty();
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        String input = "[]{}";
        ValidParentheses v = new ValidParentheses();
        System.out.println("Is valid: " + v.isValid(input));
    }
}
