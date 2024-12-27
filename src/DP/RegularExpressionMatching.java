package DP;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/regular-expression-matching/
public class RegularExpressionMatching {
    // memorization
    Map<String, Boolean> cache = new HashMap<>(); // key: length of s:p

    // top down traversing the tree
    public boolean isMatch(String s, String p) {
        String key = s.length() + ":" + p.length();
        if (cache.get(key) != null) {
            return cache.get(key);
        }

        if (p.length() == 0) { // ending case
            return s.length() == 0;
        }

        if (p.length() > 1 && p.charAt(1) == '*') { // second char is '*'
            if (isMatch(s, p.substring(2))) { // when * represents 0 previous char, skip the current `<char>*` pattern
                cache.put(key, true);
                return true;
            }

            if (s.length() > 0 && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.')) { // when * represents > 0 previous char, check if the first char matches
                boolean isMatch = isMatch(s.substring(1), p); // if matched, move onto the next char in s
                cache.put(key, isMatch);
                return isMatch;
            }
        } else {                                     // second char is not '*'
            if (s.length() > 0 && (p.charAt(0) == '.' || s.charAt(0) == p.charAt(0))) { // the first char must match in order to proceed
                boolean isMatch = isMatch(s.substring(1), p.substring(1));
                cache.put(key, isMatch);
                return isMatch;
            }
        }
        return false; // other cases should not match
    }

    public boolean isMatchDP(String s, String p) {
        if (p == null || p.length() == 0) return (s == null || s.length() == 0);

        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[0][0] = true;
        for (int j = 2; j <= p.length(); j++) {
            dp[0][j] = p.charAt(j - 1) == '*' && dp[0][j - 2];
        }

        for (int j = 1; j <= p.length(); j++) {
            for (int i = 1; i <= s.length(); i++) {
                if (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.')
                    dp[i][j] = dp[i - 1][j - 1];
                else if (p.charAt(j - 1) == '*')
                    dp[i][j] = dp[i][j - 2] || ((s.charAt(i - 1) == p.charAt(j - 2) || p.charAt(j - 2) == '.') && dp[i - 1][j]);
            }
        }
        return dp[s.length()][p.length()];
    }

    public static void main(String[] args) {
        RegularExpressionMatching r = new RegularExpressionMatching();
        String s = "aab", p = "c*a*";
        System.out.println(r.isMatch(s, p));
        System.out.println(r.isMatchDP(s, p));
    }
}
