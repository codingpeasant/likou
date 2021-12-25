package DP;

// https://leetcode.com/problems/house-robber-ii/
public class HouseRob2 {
    public int rob(int[] nums) {
        if (nums.length == 0)
            return 0;
        if (nums.length < 2)
            return nums[0];

        int[] startFromFirstHouse = new int[nums.length];
        int[] startFromSecondHouse = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                startFromFirstHouse[i] = nums[i];
                startFromSecondHouse[i] = 0;
            } else if (i == 1) {
                startFromFirstHouse[i] = Math.max(startFromFirstHouse[i - 1], nums[i]);
                startFromSecondHouse[i] = nums[i];;
            } else if (i == nums.length - 1) { // only applicable for start second house
                startFromSecondHouse[i] = Math.max(startFromSecondHouse[i - 2] + nums[i], startFromSecondHouse[i - 1]);
            } else {
                startFromFirstHouse[i] = Math.max(startFromFirstHouse[i - 2] + nums[i], startFromFirstHouse[i - 1]);
                startFromSecondHouse[i] = Math.max(startFromSecondHouse[i - 2] + nums[i], startFromSecondHouse[i - 1]);
            }
        }

        return Math.max(startFromFirstHouse[nums.length - 2], startFromSecondHouse[nums.length - 1]);
    }

    public static void main(String args[]) {
        HouseRob2 h = new HouseRob2();
        int[] input = {200,7,9,100,2};
        System.out.println("Max money: " + h.rob(input));
    }
}
