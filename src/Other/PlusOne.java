package Other;

import java.util.Arrays;

// https://leetcode.com/problems/plus-one/
public class PlusOne {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i]++;
                break;
            } else {
                digits[i] = 0;
            }
        }
        if (digits[0] == 0) {
            int[] res = new int[digits.length + 1];
            res[0] = 1;
            return res;
        }
        return digits;
    }

    public static void main(String args[]) {
        PlusOne p = new PlusOne();
        int[] input = {9, 9, 9, 9};
        System.out.println("Plus one: " + Arrays.toString(p.plusOne(input)));
    }
}

