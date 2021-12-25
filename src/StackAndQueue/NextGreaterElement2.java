package StackAndQueue;

import java.util.Arrays;
import java.util.Stack;

// https://leetcode.com/problems/next-greater-element-ii/
public class NextGreaterElement2 {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Arrays.fill(res, -1);
        Stack<Integer> maxStack = new Stack<>();

        for (int i = 0; i < nums.length * 2; i++) {
            while (!maxStack.isEmpty() && nums[i % nums.length] > nums[maxStack.peek()]) {
                res[maxStack.pop()] = nums[i % nums.length];
            }
            maxStack.push(i % nums.length);
        }

        return res;
    }

    public static void main(String[] args) {
        NextGreaterElement2 n = new NextGreaterElement2();
        int[] nums2 = {
                100,1,11,1,120,111,123,1,-1,-100
        };

        System.out.println(Arrays.toString(n.nextGreaterElements(nums2)));
    }
}
