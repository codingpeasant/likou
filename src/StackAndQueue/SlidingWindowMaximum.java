package StackAndQueue;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

// https://leetcode.com/problems/sliding-window-maximum/
public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) {
            return new int[0];
        }
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int ri = 0;
        // store index
        Deque<Integer> q = new LinkedList<>();
        for (int i = 0; i < nums.length; i++) {
            // remove numbers out of range k
            while (!q.isEmpty() && q.peek() < i - k + 1) {
                q.poll();
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && nums[q.peekLast()] < nums[i]) {
                q.pollLast();
            }
            // q contains index... r contains content
            q.offer(i);
            if (i >= k - 1) {
                res[ri++] = nums[q.peek()];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        SlidingWindowMaximum s = new SlidingWindowMaximum();
        System.out.println(Arrays.toString(s.maxSlidingWindow(nums, 3)));
    }
}
