package Other;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/verifying-an-alien-dictionary/
public class VerifyAlientDic {

    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> charToSequence = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            charToSequence.put(order.charAt(i), i);
        }

        for (int i = 1; i < words.length; i++) {
            if (!isBigger(words[i - 1], words[i], charToSequence)) {
                return false;
            }
        }
        return true;
    }

    private boolean isBigger(String word1, String word2, Map<Character, Integer> charToSequence) {
        int len1 = word1.length();
        int len2 = word2.length();
        for (int i = 0; i < len1 && i < len2; i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                return charToSequence.get(word2.charAt(i)) > charToSequence.get(word1.charAt(i));
            }
        }

        return len1 <= len2;
    }

    public static void main(String[] args) {
        VerifyAlientDic v = new VerifyAlientDic();
        String order = "abcdefghijklmnopqrstuvwxyz";
        System.out.println(v.isAlienSorted(new String[]{"apple","apple"}, order));
    }
}