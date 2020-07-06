package DP;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class WordBreak {
    public boolean wordBreak(String s, List<String> dict) {
        // DFS
        Set<Integer> set = new HashSet<Integer>();
        return dfs(s, 0, new HashSet<>(dict), set);
    }

    // easier to understand
    private boolean dfs(String s, int index, Set<String> dict, Set<Integer> set){
        // base case
        if(index == s.length()) return true;
        // check memory
        if(set.contains(index)) return false;
        // recursion
        for(int i = index+1;i <= s.length();i++){
            String t = s.substring(index, i);
            if(dict.contains(t))
                if(dfs(s, i, dict, set))
                    return true;
                else
                    set.add(i);
        }
        set.add(index);
        return false;
    }

    public boolean wordBreakDP(String s, List<String> dict) {
        boolean[] f = new boolean[s.length() + 1];

        f[0] = true;
        for(int i = 1; i <= s.length(); i++){
            for(String str: dict){
                if(str.length() <= i){
                    if(f[i - str.length()]){
                        if(s.startsWith(str, i-str.length())){
                            f[i] = true;
                            break;
                        }
                    }
                }
            }
        }

        return f[s.length()];
    }

    public static void main(String[] args) {
        String s = "leetcode";
        List<String> dict = Arrays.asList("leet", "code", "sand", "and", "cat");
        WordBreak w = new WordBreak();
        System.out.println("Exists: " + w.wordBreak(s, dict) + "; " + w.wordBreakDP(s, dict));
    }
}
