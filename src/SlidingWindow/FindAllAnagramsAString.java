package SlidingWindow;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/find-all-anagrams-in-a-string/
// Same with https://leetcode.com/problems/permutation-in-string/, https://leetcode.com/problems/minimum-window-substring/
public class FindAllAnagramsAString {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int left = 0;
        int right = 0;
        Map<Character, Integer> charsCount = new HashMap<>();
        for (char element: p.toCharArray()) {
            charsCount.put(element, charsCount.getOrDefault(element, 0) + 1);
        }
        int moreCharsNeeded = charsCount.size();

        while (right < s.length()) {
            char rightChar = s.charAt(right);
            if (charsCount.get(rightChar) != null) {
                charsCount.put(rightChar, charsCount.getOrDefault(rightChar, 0) - 1);
                if (charsCount.get(rightChar) == 0) { // all occurrences of this char is included
                    moreCharsNeeded--;
                }
            }
            right++;

            while (moreCharsNeeded == 0) {
                if (right - left == p.length()) {
                    res.add(left);
                }

                char leftChar = s.charAt(left);
                if (charsCount.get(leftChar) != null) {
                    charsCount.put(leftChar, charsCount.getOrDefault(leftChar, 0) + 1);
                    if (charsCount.get(leftChar) == 1) { // from 0 to 1
                        moreCharsNeeded++;
                    }
                }
                left++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        FindAllAnagramsAString f = new FindAllAnagramsAString();
        String s = "baa";
        String p = "aa";
        f.findAnagrams(s, p).forEach(System.out::println);
    }
}
