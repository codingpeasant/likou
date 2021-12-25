package Other;

// https://leetcode.com/problems/trapping-rain-water/
public class TrappingRainWater {
    public int trap(int[] height) { // O(n^2)
        if (height == null || height.length == 0) return 0;

        int res = 0;
        for (int i = 0; i < height.length; i++) {
            int leftMax = 0, rightMax = 0;
            for (int j = 0; j < i; j++) {
                leftMax = Math.max(leftMax, height[j]);
            }

            for (int j = i + 1; j< height.length; j++) {
                rightMax = Math.max(rightMax, height[j]);
            }

            int currentWater = Math.min(leftMax, rightMax) - height[i];
            if (currentWater > 0) res += currentWater;
        }

        return res;
    }

    public int trapMemorization(int[] height) { // O(n)
        if (height == null || height.length == 0) return 0;

        int res = 0;
        int[] leftMaxAt = new int[height.length];
        int[] rightMaxAt = new int[height.length];

        int maxSoFar = -1;
        for (int i = 0; i < height.length; i++) {
            maxSoFar = Math.max(maxSoFar, height[i]);
            leftMaxAt[i] = maxSoFar;
        }
        
        maxSoFar = -1;
        for (int i = height.length - 1; i >=0;i--) {
            maxSoFar = Math.max(maxSoFar, height[i]);
            rightMaxAt[i] = maxSoFar;
        }

        for (int i = 1; i < height.length - 1; i++) {
            int currentWater = Math.min(leftMaxAt[i - 1], rightMaxAt[i + 1]) - height[i];
            if (currentWater > 0) res += currentWater;
        }

        return res;
    }

    public static void main(String[] args) {
        TrappingRainWater t = new TrappingRainWater();
        int[] input = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.println(t.trap(input));
        System.out.println(t.trapMemorization(input));
    }
}
