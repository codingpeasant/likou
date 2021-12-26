package Other;

import java.util.HashSet;

// https://leetcode.com/problems/longest-palindrome/
public class LongestPalindrome {
    public int longestPalindrome(String s) {
        if (s == null || s.length() == 0) return 0;
        HashSet<Character> hs = new HashSet<>();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (hs.contains(s.charAt(i))) {
                hs.remove(s.charAt(i)); // if there was a matching before, add 1 palindrome
                count++;
            } else {
                hs.add(s.charAt(i));
            }
        }
        if (!hs.isEmpty()) return count * 2 + 1; // pick one left in the set as the center of the palindrome string
        return count * 2;
    }

    public static void main(String args[]) {
        LongestPalindrome l = new LongestPalindrome();
        String str = "bbbbaabaa";
        System.out.println(l.longestPalindrome(str));
    }
}
