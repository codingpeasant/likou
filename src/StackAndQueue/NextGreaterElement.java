package StackAndQueue;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// https://leetcode.com/problems/next-greater-element-i/
public class NextGreaterElement {
    // We use a stack to keep a decreasing sub-sequence,
    // whenever we see a number x greater than stack.peek() we pop all elements less than x and for all the popped ones, their next greater element is x
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> resMap = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        for (int num:nums2) {
            while (!stack.isEmpty() && num > stack.peek()) {
                resMap.put(stack.pop(), num);
            }
            stack.push(num);
        }

        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = resMap.getOrDefault(nums1[i], -1); // this only works when there is no dup values in the nums array
        }

        return nums1;
    }

    public static void main(String args[]) {
        NextGreaterElement n = new NextGreaterElement();
        int[] nums1 = {
                3,7,4,8
        };

        int[] nums2 = {
                3,2,1,5,7,4,8
        };

        System.out.println(Arrays.toString(n.nextGreaterElement(nums1, nums2)));
    }
}
