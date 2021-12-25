package Other;

// https://leetcode.com/problems/range-sum-query-immutable/
public class RangeSumQueryImmutable {
    private int[] preSum;

    public RangeSumQueryImmutable(int[] nums) {
        // preSum[0] = 0，便于计算累加和
        preSum = new int[nums.length + 1];
        // 计算 nums 的累加和
        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
    }

    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }

    public static void main(String[] args) {
        int[] nums = {-2, 0, 3, -5, 2, -1};
        RangeSumQueryImmutable r = new RangeSumQueryImmutable(nums);

        System.out.println(r.sumRange(3, 5));
    }
}
