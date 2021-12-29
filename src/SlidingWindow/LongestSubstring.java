package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/longest-substring-without-repeating-characters/
public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        int left = 0;
        int right = 0;
        int longestLength = Integer.MIN_VALUE;
        Map<Character, Integer> charCount = new HashMap<>();

        while (right < s.length()) {
            Character rightChar = s.charAt(right);
            charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);
            if (charCount.get(rightChar) == 1) {
                longestLength = Math.max(longestLength, right - left + 1);
            }
            right++;

            while (charCount.get(rightChar) > 1) {
                Character leftChar = s.charAt(left);
                charCount.put(leftChar, charCount.get(leftChar) - 1);
                left++;
            }
        }

        return longestLength;
    }

    public int lengthOfLongestSubstring2(String s) {
        if (s.length() == 0) return 0;
        HashMap<Character, Integer> charIndex = new HashMap<>(); // char:index position
        int max = 0;
        for (int i = 0, j = 0; i < s.length(); ++i) {
            if (charIndex.containsKey(s.charAt(i))) {
                j = Math.max(j, charIndex.get(s.charAt(i)) + 1);
            }
            charIndex.put(s.charAt(i), i);
            max = Math.max(max, i - j + 1);
        }
        return max;
    }

    public static void main(String[] args) {
        LongestSubstring mdt = new LongestSubstring();
        String input = "pwwkew";
        System.out.println("Max length: " + mdt.lengthOfLongestSubstring(input));
    }
}
