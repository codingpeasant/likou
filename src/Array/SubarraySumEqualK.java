package Array;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/subarray-sum-equals-k/
// sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1
// cannot use sliding window because all previous sum are needed
public class SubarraySumEqualK {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int sum = 0;
        Map<Integer, Integer> sumCount = new HashMap<>(); // presum
        sumCount.put(0, 1); // this is used when sum == k

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sumCount.containsKey(sum - k)) { // similar with 2Sum
                res += sumCount.get(sum - k);
            }
            sumCount.put(sum, sumCount.getOrDefault(sum, 0) + 1);

        }
        return res;
    }

    public int subarraySum2(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum = 0;
            for (int end = start; end < nums.length; end++) {
                sum += nums[end];
                if (sum == k)
                    System.out.println(start + "/" + end);
                count++;
            }
        }
        return count;
    }

    public static void main(String args[]) {
        SubarraySumEqualK s = new SubarraySumEqualK();
        int[] input = {1, 1, 1, 1, 1, -1, 1, 1, 1, 2};
        System.out.println(s.subarraySum(input, 5));
        System.out.println(s.subarraySum2(input, 5));
    }
}
