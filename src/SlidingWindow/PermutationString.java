package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/permutation-in-string/
public class PermutationString {
    public boolean checkInclusion(String s1, String s2) {
        int left = 0;
        int right = 0;
        int countNeeded = s1.length();
        Map<Character, Integer> charsCountNeeded = new HashMap<>();
        for (char charNeeded : s1.toCharArray()) {
           charsCountNeeded.put(charNeeded, charsCountNeeded.getOrDefault(charNeeded, 0) + 1);
        }

        while (right < s2.length()) {
            char rightChar = s2.charAt(right);
            if (charsCountNeeded.get(rightChar) != null) {
                charsCountNeeded.put(rightChar, charsCountNeeded.getOrDefault(rightChar, 0) - 1);
                if (charsCountNeeded.get(rightChar) >= 0) {
                    countNeeded--;
                }
            }
            right++;

            while (countNeeded == 0) {
                if (right - left == s1.length()) {
                    return true;
                }
                char leftChar = s2.charAt(left);
                if (charsCountNeeded.get(leftChar) != null) {
                    charsCountNeeded.put(leftChar, charsCountNeeded.getOrDefault(leftChar, 0) + 1);
                    if (charsCountNeeded.get(leftChar) > 0) {
                        countNeeded++;
                    }
                }
                left++;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        PermutationString p = new PermutationString();
        String s1 = "ab";
        String s2 = "eidbbaooo";
        System.out.println(p.checkInclusion(s1, s2));
    }
}
