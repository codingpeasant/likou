package Other;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/happy-number/
public class HappyNumber {
    public boolean isHappy(int n) {
        Set<Integer> inLoop = new HashSet<>();
        // it loops endlessly in a cycle so dup appears
        while (inLoop.add(n)) {
            int sum = getSquareSum(n);
            if (sum == 1) {
                return true;
            } else {
                n = sum;
            }
        }

        return false;
    }

    private int getSquareSum(int n) {
        int sum = 0, remain;
        while (n > 0) {
            remain = n % 10;
            sum += remain * remain;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        HappyNumber h = new HappyNumber();
        int input = 19;
        System.out.println("is happy: " + h.isHappy(input));
    }
}
