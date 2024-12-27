package DP;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// https://leetcode.com/problems/word-break/
public class WordBreak {
    public boolean wordBreak(String s, List<String> dict) {
        // DFS
        Set<Integer> set = new HashSet<>();
        return dfs(s, 0, new HashSet<>(dict), set);
    }

    private boolean dfs(String s, int index, Set<String> dict, Set<Integer> set) {
        // base case
        if (index == s.length()) return true;
        // check memory
        if (set.contains(index)) return false;
        // recursion
        for (int i = index + 1; i <= s.length(); i++) {
            String t = s.substring(index, i);
            if (dict.contains(t))
                if (dfs(s, i, dict, set))
                    return true;
                else
                    set.add(i);
        }
        set.add(index);
        return false;
    }

    // easier to understand
    public boolean wordBreakDP(String s, List<String> dict) {
        boolean[] f = new boolean[s.length() + 1];

        f[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (f[j] && dict.contains(s.substring(j, i))) {
                    f[i] = true;
                    break;
                }
            }
        }

        return f[s.length()];
    }

    public static void main(String[] args) {
        String s = "leetcode";
        List<String> dict = Arrays.asList("l", "leet", "code", "sand", "and", "cat");
        WordBreak w = new WordBreak();
        System.out.println("Exists: " + w.wordBreak(s, dict) + "; " + w.wordBreakDP(s, dict));
    }
}
