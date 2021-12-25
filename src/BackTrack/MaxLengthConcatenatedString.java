package BackTrack;

import java.util.*;

// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
public class MaxLengthConcatenatedString {
    public int maxLength(List<String> arr) {
        int maxLen = 0;
        List<String> buckets = new ArrayList<>();
        buckets.add(""); // add empty bucket
        for (int i = 0; i < arr.size(); i++) {
            int n = buckets.size();
            for (int j = 0; j < n; j++) {
                if (isOkay(buckets.get(j), arr.get(i))) {
                    String newString = buckets.get(j) + arr.get(i);
                    buckets.add(newString);
                    maxLen = Math.max(newString.length(), maxLen);
                }
            }
        }

        return maxLen;
    }

    int dfsMax = 0;

    public int maxLengthDFS(List<String> arr) {
        dfs(0, arr, "");
        return dfsMax;
    }

    public void dfs(int start, List<String> arr, String str) {
        if (!isUnique(str)) {
            return;
        }
        dfsMax = Math.max(dfsMax, str.length());

        for (int i = start; i < arr.size(); i++) {
            String s = arr.get(i);
            dfs(i + 1, arr, str + s);
        }
    }

    private boolean isUnique(String s) {
        Set<Character> set = new HashSet<>();

        for (char ch : s.toCharArray()) {
            if (set.contains(ch)) {
                return false;
            }
            set.add(ch);
        }
        return true;
    }

    private boolean isOkay(String a, String b) {
        Map<String, Integer> charCount = new HashMap<>();

        for (int i = 0; i < a.length(); i++) {
            String cha = String.valueOf(a.charAt(i));
            if (charCount.containsKey(cha)) {
                return false;
            } else {
                charCount.put(cha, 1);
            }
        }

        for (int i = 0; i < b.length(); i++) {
            String cha = String.valueOf(b.charAt(i));
            if (charCount.containsKey(cha)) {
                return false;
            } else {
                charCount.put(cha, 1);
            }
        }
        return true;
    }

    // Driver method
    public static void main(String[] args) {
        ArrayList<String> wordList = new ArrayList<>(Arrays.asList("cha", "r", "act", "ers"));

        MaxLengthConcatenatedString m = new MaxLengthConcatenatedString();
        System.out.println("Maximum possible length: " + m.maxLength(wordList));
        System.out.println("Maximum possible length: " + m.maxLengthDFS(wordList));
    }
}
