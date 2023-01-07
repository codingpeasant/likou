package SlidingWindow;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class MaximumNumberOccurrencesSubstring {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        if (s.length() == 0) return 0;
        Map<String, Integer> strCount = new HashMap<>();
        int max = 0;

        int left = 0, right;
        while (left < s.length()) {
            Map<Character, Integer> charCount = new HashMap<>();
            for (right = left; right - left + 1 <= minSize && right < s.length(); right++) {
                Character rightChar = s.charAt(right);
                charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);
            }

            while (right - left >= minSize && right - left <= maxSize && charCount.size() <= maxLetters && right <= s.length()) {
                String cur = s.substring(left, right);
                strCount.put(cur, strCount.getOrDefault(cur, 0) + 1);
                max = Math.max(max, strCount.get(cur));
                right++;
                if (right >= s.length() - 1) break;
                Character rightChar = s.charAt(right);
                charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);
            }
            left++;
        }
        return max;
    }

    public static void main(String[] args) {
        MaximumNumberOccurrencesSubstring m = new MaximumNumberOccurrencesSubstring();
        String input = "aababcaab";
        System.out.println(m.maxFreq(input, 2, 3, 4));
    }
}
