package Other;

// https://leetcode.com/problems/container-with-most-water/
// Greedy
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) // keep the higher
                l++;
            else
                r--;
        }
        return maxarea;
    }

    public static void main(String[] args) {
        ContainerWithMostWater c = new ContainerWithMostWater();
        int[] input = {1,8,6,2,5,4,8,3,7};
        System.out.println("Max water: " + c.maxArea(input));
    }
}
