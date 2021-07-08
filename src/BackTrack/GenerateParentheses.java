package BackTrack;

import java.util.ArrayList;
import java.util.List;
// https://leetcode.com/problems/generate-parentheses/
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> solution = new ArrayList<>();

        if (n == 0) {
            return solution;
        }
        find(solution, "", 0, 0, n);
        return solution;

    }

    public void find(List<String> solution, String cur, int open, int close, int max) {
        if (cur.length() == max * 2) {
            solution.add(cur);
            return;
        }

        if (open < max) {
            find(solution, cur + "(", open + 1, close, max);
        }

        if (close < open) {
            find(solution, cur + ")", open, close + 1, max);
        }
    }

    public static void main(String[] args) {
        GenerateParentheses mdt = new GenerateParentheses();
        for (String parenthesis : mdt.generateParenthesis(3)) {
            System.out.println(parenthesis);
        }
    }
}
