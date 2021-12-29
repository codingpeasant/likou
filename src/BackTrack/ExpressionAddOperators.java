package BackTrack;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/expression-add-operators/
public class ExpressionAddOperators {
    public List<String> addOperators(String num, int target) {
        List<String> rst = new ArrayList<>();
        if (num == null || num.length() == 0) return rst;
        helper(rst, "", num, target, 0, 0, 0);
        return rst;
    }

    public void helper(List<String> rst, String path, String num, int target, int pos, long previousEval, long previousValue) {
        if (pos == num.length()) {
            if (target == previousEval)
                rst.add(path);
            return;
        }
        for (int i = pos; i < num.length(); i++) {
            if (i != pos && num.charAt(pos) == '0') break; // don't accept leading zeros
            long cur = Long.parseLong(num.substring(pos, i + 1)); // 2,3,2/2,32/23,2/232
            if (pos == 0) {
                helper(rst, path + cur, num, target, i + 1, cur, cur);
            } else {
                helper(rst, path + "+" + cur, num, target, i + 1, previousEval + cur, cur);

                helper(rst, path + "-" + cur, num, target, i + 1, previousEval - cur, -cur);

                // going backward and re-eval. e.g. 2+3*2: previousEval = 5 (2+3); previousValue = 3; current eval = 5 - 3 + 3 * 2
                helper(rst, path + "*" + cur, num, target, i + 1, previousEval - previousValue + previousValue * cur, previousValue * cur);
            }
        }
    }

    public static void main(String[] args) {
        ExpressionAddOperators e = new ExpressionAddOperators();
        String input = "232";
        List<String> res = e.addOperators(input, 8);
        res.forEach(System.out::println);
    }
}
