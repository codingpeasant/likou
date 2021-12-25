package Other;

import java.util.Arrays;

// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
public class TwoSum2 {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;

        while (i < j) {
            if (numbers[i] + numbers[j] > target) {
                j--;
            } else if (numbers[i] + numbers[j] < target) {
                i++;
            } else {
                return new int[]{i + 1, j + 1};
            }
        }
        return new int[2];
    }

    public static void main(String[] args) {
        TwoSum2 t = new TwoSum2();
        int[] numbers = {2, 7, 11, 15};
        System.out.println(Arrays.toString(t.twoSum(numbers, 9)));
    }

}
