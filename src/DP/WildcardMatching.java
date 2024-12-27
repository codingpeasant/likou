package DP;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/wildcard-matching/
// similar with RegularExpressionMatching
public class WildcardMatching {
    Map<String, Boolean> cache = new HashMap<>();

    public boolean isMatch(String s, String p) {
        String key = s.length() + ":" + p.length();
        if (cache.containsKey(key)) {
            return cache.get(key);
        }

        if (p.length() == 0 || p == "*") { // when p exhausts or p is only * that could match anything
            return s.length() == 0;
        }

        if (p.charAt(0) == '*') {
            // match * with the first char of s OR match * with 0 char (skip it)
            boolean isMatch = (s.length() >= 1 && isMatch(s.substring(1), p)) || isMatch(s, p.substring(1));
            cache.put(key, isMatch);
            return isMatch;
        } else if (s.length() > 0 && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '?')) {
            // first char is the same, move both forward
            boolean isMatch = isMatch(s.substring(1), p.substring(1));
            cache.put(key, isMatch);
            return isMatch;
        }
        cache.put(key, false);
        return false;
    }

    public boolean isMatchDP(String s, String p) {
        int m = s.length(), n = p.length();
        char[] ws = s.toCharArray();
        char[] wp = p.toCharArray();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int j = 1; j <= n; j++)
            dp[0][j] = dp[0][j - 1] && wp[j - 1] == '*';
        for (int i = 1; i <= m; i++)
            dp[i][0] = false;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (wp[j - 1] == '?' || ws[i - 1] == wp[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else if (wp[j - 1] == '*')
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            }
        }
        return dp[m][n];
    }

    public static void main(String[] args) {
        WildcardMatching w = new WildcardMatching();
        String s = "adceb", p = "*a*b";
        System.out.println(w.isMatchDP(s, p));
        System.out.println(w.isMatch(s, p));
    }
}
