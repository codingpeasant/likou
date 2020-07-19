package DFS;

import java.util.*;

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

    public int maxLengthDFS(List<String> arr) {
        return check(arr, "", 0, 0);
    }

    // DFS or DP?
    private int check(List<String> arr, String set, int pos, int sum) {
        if (pos == arr.size()) {
            return sum;
        }

        String curStr = arr.get(pos);
        String previousSet = set;

        for (int i = 0; i < curStr.length(); i++) {
            char c = curStr.charAt(i);
            if (set.contains(String.valueOf(c))) {
                set = previousSet; // if this letter appears before, reverse the set
                break;
            } else {
                set += String.valueOf(c); // append the letter
            }
        }

        if (set == previousSet) {//this word is not allowed to use, so just check the result without it
            return check(arr, set, pos + 1, sum);
        } else {//this word is allowed to use, then 2 senarios should be checked, with it or without it.
            return Math.max(check(arr, previousSet, pos + 1, sum), check(arr, set, pos + 1, sum + curStr.length()));
        }
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
        ArrayList<String> wordList = new ArrayList<>(Arrays.asList("cha","r","act","ers"));

        MaxLengthConcatenatedString m = new MaxLengthConcatenatedString();
        System.out.println("Maximum possible length: " + m.maxLength(wordList));
        System.out.println("Maximum possible length: " + m.maxLengthDFS(wordList));
    }
}
