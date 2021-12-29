package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/remove-duplicate-letters/
public class RemoveDuplicateLetters {
    public String removeDuplicateLetters(String s) {
        // min stack to keep the smallest lexicographical substring
        Stack<Character> stack = new Stack<>();
        int[] count = new int[26]; // make sure there is no character missed when popping the char from the stack
        char[] arr = s.toCharArray();
        for (char c : arr) {
            count[c - 'a']++;
        }
        boolean[] visited = new boolean[26]; // make sure unique characters in the stack
        for (char c : arr) {
            count[c - 'a']--;
            if (visited[c - 'a']) {
                continue;
            }
            // got a smaller char and there is another stack.peek() later
            // pop the larger char
            while (!stack.isEmpty() && stack.peek() > c && count[stack.peek() - 'a'] > 0) {
                visited[stack.peek() - 'a'] = false;
                stack.pop();
            }
            stack.push(c);
            visited[c - 'a'] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        RemoveDuplicateLetters r = new RemoveDuplicateLetters();
        System.out.println(r.removeDuplicateLetters("cbacdcbc"));
    }
}
