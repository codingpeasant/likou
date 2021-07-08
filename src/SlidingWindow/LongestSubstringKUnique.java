package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

// https://www.programcreek.com/2013/02/longest-substring-which-contains-2-unique-characters/
public class LongestSubstringKUnique {
    public String findLongestSubstring(String str, int k) {
        int right = 0;
        int left = 0;
        String longestSubString = "";

        Map<Character, Integer> charNumber = new HashMap<>();

        while (right < str.length()) {
            char rightChar = str.charAt(right);
            charNumber.put(rightChar, charNumber.getOrDefault(rightChar, 0) + 1);
            if(charNumber.size() == k && longestSubString.length() < right - left + 1) {
                longestSubString = str.substring(left, right + 1);
            }
            right++;

            while (charNumber.size() > k) {
                char leftChar = str.charAt(left);
                if (charNumber.get(leftChar) == 1) {
                    charNumber.remove(leftChar);
                } else {
                    charNumber.put(leftChar, charNumber.get(leftChar) - 1);
                }
                left++;
            }
        }

        return longestSubString;
    }

    public static void main(String[] args) {
        LongestSubstringKUnique l = new LongestSubstringKUnique();
        String input = "abcadcacacaca";
        System.out.println("Max length: " + l.findLongestSubstring(input, 3));
        String input2 = "abcbbbbcccbdddadacb";
        System.out.println("Max length: " + l.findLongestSubstring(input2, 2));
    }
}
