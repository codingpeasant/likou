package BackTrack;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/restore-ip-addresses/
public class RestoreIPAddresses {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        helper(s, "", res, 0);
        return res;
    }

    public void helper(String s, String tmp, List<String> res, int n) {
        if (n == 4) {
            if (s.length() == 0) res.add(tmp.substring(0, tmp.length() - 1));
            //substring here to get rid of last '.'
            return;
        }

        for (int k = 1; k <= 3; k++) {
            if (s.length() < k) continue;
            int val = Integer.parseInt(s.substring(0, k));
            if (val > 255 || k != String.valueOf(val).length()) continue;
            /*in the case 010 the parseInt will return len=2 where val=10, but k=3, skip this.*/
            helper(s.substring(k), tmp + s.substring(0, k) + ".", res, n + 1);
        }
    }

    public List<String> restoreIpAddresses1(String s) {
        List<String> res = new ArrayList<>();
        backtrack(s, "", 0, 0, res);
        return res;
    }

    private void backtrack(String s, String cur, int starting, int n, List<String> res) { // n to track how many parts so far
        if (n == 4 && cur.length() == s.length() + 4) {
            res.add(cur.substring(0, cur.length() - 1)); // remove '.'
            return;
        }

        if (n > 4) return; // e.g. 2.5.5.25511135

        for (int i = 1; i <= 3; i++) { // try to include 1 or 2 or 3 digits
            if (starting + i > s.length()) break;
            String substring = s.substring(starting, starting + i); // include the first char not the last
            int val = Integer.parseInt(substring);
            if (val > 255 || String.valueOf(val).length() != i) continue; // e.g. 265 or 02
            backtrack(s, cur + substring + ".", starting + i, n + 1, res); // valid so far,
        }
    }

    public static void main(String args[]) {
        RestoreIPAddresses r = new RestoreIPAddresses();
        String input = "25525511135";
        System.out.println(r.restoreIpAddresses1(input));
    }
}
