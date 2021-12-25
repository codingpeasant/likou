package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/minimum-window-substring/
public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        int left = 0;
        int right = 0;
        int minLeft = 0;
        int minLength = Integer.MAX_VALUE;
        int moreCharsNeededToIncludeAll = t.length();

        Map<Character, Integer> charCountNeeded = new HashMap<>(); // stores ASCII - 128 max; needed when t has duplicate letters; can be HashMap
        for (char currentChar: t.toCharArray()) {
            charCountNeeded.put(currentChar, charCountNeeded.getOrDefault(currentChar,0) + 1); // need this many chars
        }

        while (right < s.length()) {
            final char rightChar = s.charAt(right);
            if (charCountNeeded.get(rightChar) != null) {
                charCountNeeded.put(rightChar, charCountNeeded.getOrDefault(rightChar,0) - 1);
                if (charCountNeeded.get(rightChar) >= 0) {
                    moreCharsNeededToIncludeAll--; // if exist and >=0, it means a needed char was added
                }
            }
            right++;

            while (moreCharsNeededToIncludeAll == 0) {
                if (minLength > right - left) {
                    minLength = right - left;
                    minLeft = left;
                }
                final char leftChar = s.charAt(left);
                if (t.contains(String.valueOf(leftChar))) {
                    charCountNeeded.put(leftChar, charCountNeeded.getOrDefault(leftChar,0) + 1); // more needed
                    if (charCountNeeded.get(leftChar) > 0) { // if more than 0 needed
                        moreCharsNeededToIncludeAll++;
                    }
                }
                left++;
            }
        }
        return minLength == Integer.MAX_VALUE ? "" : s.substring(minLeft, minLeft + minLength);
    }

    public static void main(String[] args) {
        MinimumWindowSubstring m = new MinimumWindowSubstring();
        String s = "ADOBECODEBANC";
        String t = "AABC";
        System.out.println(m.minWindow(s, t));
    }
}
