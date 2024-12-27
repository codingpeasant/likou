package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/sum-of-subarray-minimums/
//        I guess this is a general intuition for most solution.
//        res = sum(A[i] * f(i))
//        where f(i) is the number of subarrays,
//        in which A[i] is the minimum.
//
//        To get f(i), we need to find out:
//        left[i], the length of strict bigger numbers on the left of A[i],
//        right[i], the length of bigger numbers on the right of A[i].
//
//        Then,
//        left[i] + 1 equals to
//        the number of subarray ending with A[i],
//        and A[i] is single minimum.
//
//        right[i] + 1 equals to
//        the number of subarray starting with A[i],
//        and A[i] is the first minimum.
//
//        Finally f(i) = (left[i] + 1) * (right[i] + 1)

public class SumSubarrayMinimums {
    public int sumSubarrayMins(int[] A) {
        long res = 0, mod = (int) 1e9 + 7;
        int n = A.length, left[] = new int[n], right[] = new int[n];
        Stack<int[]> s1 = new Stack<>(), s2 = new Stack<>();
        for (int i = 0; i < n; ++i) {
            int count = 1;
            while (!s1.isEmpty() && s1.peek()[0] > A[i])
                count += s1.pop()[1];
            s1.push(new int[]{A[i], count});
            left[i] = count;
        }
        for (int i = n - 1; i >= 0; --i) {
            int count = 1;
            while (!s2.isEmpty() && s2.peek()[0] >= A[i])
                count += s2.pop()[1];
            s2.push(new int[]{A[i], count});
            right[i] = count;
        }
        for (int i = 0; i < n; ++i)
            res = (res + (long) A[i] * left[i] * right[i]) % mod;
        return (int) res;
    }

    public static void main(String[] args) {
        SumSubarrayMinimums s = new SumSubarrayMinimums();
        int[] input = {3, 1, 2, 4};
        System.out.println(s.sumSubarrayMins(input));
    }
}
