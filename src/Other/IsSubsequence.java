package Other;

// https://leetcode.com/problems/is-subsequence/
public class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        if (s.equals("")) return true;
        int j = 0;
        for (int i = 0; i < t.length(); i++) {
            if (t.charAt(i) == s.charAt(j)) {
                j++;
            }
            if (j == s.length()) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        IsSubsequence s = new IsSubsequence();
        System.out.println("Is Subsequence: " + s.isSubsequence("abc", "ahbgdc"));
    }
}
