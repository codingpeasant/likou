package Other;

import java.util.HashMap;
import java.util.Map;

// sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1
public class SubarraySumEqualK {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int sum = 0;
        Map<Integer, Integer> sumCount = new HashMap<>();
        sumCount.put(0, 1);

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sumCount.containsKey(sum - k)) {
                res += sumCount.get(sum - k);
            }
            sumCount.put(sum, sumCount.getOrDefault(sum, 0) + 1);

        }
        return res;
    }

    public static void main(String args[]) {
        SubarraySumEqualK s = new SubarraySumEqualK();
        int[] input = {1,1,1,1,1,-1,1,1,1,2};
        System.out.println(s.subarraySum(input, 5));
    }
}
