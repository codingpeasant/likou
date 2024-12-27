package Other;

// https://leetcode.com/problems/divide-two-integers/
public class DivideTwoIntegers {
    public int divide(int dividend, int divisor) {
        if (Integer.MIN_VALUE == dividend && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        int res = 0;
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
        // divisor = 3, dividend = 20
        // 3*2*2 + 3*2 = 18 ---- 1*2*2 + 1*2 = 6
        while (a - b >= 0) {
            int tmp = b;
            int count = 1;
            while (a - (tmp << 1) >= 0) { // everytime multiply by 2
                tmp <<= 1;
                count <<= 1;
            }
            a -= tmp;
            res += count;
        }
        return (dividend > 0) == (divisor > 0) ? res : -res;
    }

    public static void main(String[] args) {
        DivideTwoIntegers d = new DivideTwoIntegers();
        System.out.println(d.divide(20, -3));
    }
}
