package BackTrack;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/palindrome-partitioning/
public class PalindromePartitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> cur = new ArrayList<>();
        backtrack(s, cur, res, 0);
        return res;
    }

    // first level: a, aa, aab
    private void backtrack(String s, List<String> cur, List<List<String>> res, int startPos) {
        if (startPos > s.length() - 1) {
            res.add(new ArrayList<>(cur));
            return;
        }

        for (int i = startPos; i < s.length(); i++) {
            String curString = s.substring(startPos, i + 1);
            if (isPalindrome(curString)) {
                cur.add(curString);
                backtrack(s, cur, res, i + 1);
                cur.remove(cur.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String input) {
        int left = 0, right = input.length() - 1;
        while (left < right) {
            if (input.charAt(left) != input.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String args[]) {
        PalindromePartitioning p = new PalindromePartitioning();
        String input = "aab";
        System.out.println(p.partition(input));
    }
}
