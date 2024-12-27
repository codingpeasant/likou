package Other;

import java.util.LinkedList;
import java.util.List;

// https://leetcode.com/problems/add-to-array-form-of-integer/
public class AddArrayFormInteger {
    public List<Integer> addToArrayForm(int[] num, int k) {
        LinkedList<Integer> res = new LinkedList<>();
        int carry = 0;
        int index = num.length - 1;
        while (k > 0 || index >= 0) {
            int curK = k % 10;
            int curA = index >= 0 ? num[index] : 0;
            int curDigitSum = curK + curA + carry;
            int toBeAdded = curDigitSum % 10;
            carry = curDigitSum / 10;
            index--;
            k /= 10;
            res.addFirst(toBeAdded);
        }
        if (carry != 0) {
            res.addFirst(1);
        }
        return res;
    }

    public static void main(String[] args) {
        AddArrayFormInteger a = new AddArrayFormInteger();
        int[] num = {1, 2, 0, 0};
        int k = 993400;
        System.out.println(a.addToArrayForm(num, k));
    }
}
