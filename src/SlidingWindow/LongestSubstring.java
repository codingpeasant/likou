package SlidingWindow;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
public class LongestSubstring {
//    public int lengthOfLongestSubstring(@NotNull String s) {
//        Set<Character> existingChars = new HashSet<>();
//        int curPtr = 0;
//        int begainPtr = 0;
//        int maxLength = 0;
//
//        while (curPtr < s.length()) {
//            if (!existingChars.contains(s.charAt(curPtr))) {
//                existingChars.add(s.charAt(curPtr));
//                maxLength = Math.max(maxLength, curPtr - begainPtr + 1);
//                curPtr++;
//            } else {
//                existingChars.remove(s.charAt(begainPtr));
//                begainPtr++;
//            }
//        }
//        return maxLength;
//    }

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

    public static void main(String[] args) {
        LongestSubstring mdt = new LongestSubstring();
        String input = "abcabcbb";
        System.out.println("Max length: " + mdt.lengthOfLongestSubstring(input));
    }
}
