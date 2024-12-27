package SlidingWindow;

// https://leetcode.ca/2017-11-26-727-Minimum-Window-Subsequence/
public class MinimumWindowSubsequence {
    public String minWindow(String S, String T) {
        String window = "";
        int j = 0, min = S.length() + 1; // j is for T
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == T.charAt(j)) {
                j++;
                if (j == T.length()) { // found a valid subsequence
                    int end = i + 1;
                    j--;
                    while (j >= 0) { // going backward to find the first matching char
                        if (S.charAt(i) == T.charAt(j)) j--;
                        i--;
                    }
                    j++; // j becomes 0
                    i++; // i move forward by 1
                    if (end - i < min) {
                        min = end - i;
                        window = S.substring(i, end);
                    }
                }
            }
        }
        return window;
    }

    public static void main(String[] args) {
        MinimumWindowSubsequence m = new MinimumWindowSubsequence();
        String s = "abcdebdde";
        String t = "bde";
        System.out.println(m.minWindow(s, t)); // bcde
    }
}
