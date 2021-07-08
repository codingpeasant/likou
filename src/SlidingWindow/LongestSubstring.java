package SlidingWindow;

import java.util.HashSet;
import java.util.Set;
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> existingChars = new HashSet<>();
        int curPtr = 0;
        int begainPtr = 0;
        int maxLength = 0;

        while (curPtr < s.length()) {
            if (!existingChars.contains(s.charAt(curPtr))) {
                existingChars.add(s.charAt(curPtr));
                maxLength = Math.max(maxLength, curPtr - begainPtr + 1);
                curPtr++;
            } else {
                existingChars.remove(s.charAt(begainPtr));
                begainPtr++;
            }
        }
        return maxLength;
    }

    public static void main(String[] args) {
        LongestSubstring mdt = new LongestSubstring();
        String input = "abcadcbb";
        System.out.println("Max length: " + mdt.lengthOfLongestSubstring(input));
    }
}
