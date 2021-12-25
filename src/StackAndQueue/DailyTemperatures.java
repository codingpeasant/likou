package StackAndQueue;

import java.util.Arrays;
import java.util.Stack;

// https://leetcode.com/problems/daily-temperatures/
public class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<Integer> maxStack = new Stack<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!maxStack.isEmpty() && temperatures[i] > temperatures[maxStack.peek()]) {
                int cur = maxStack.pop();
                res[cur] = i - cur;
            }
            maxStack.push(i);
        }

        return res;
    }

    public static void main(String[] args) {
        DailyTemperatures d = new DailyTemperatures();
        int[] temps = {
                73,74,75,71,69,72,76,73
        };
        System.out.println(Arrays.toString(d.dailyTemperatures(temps)));
    }
}
