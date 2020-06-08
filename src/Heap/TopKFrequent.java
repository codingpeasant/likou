package Heap;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class TopKFrequent {
    class Pair {
        int num;
        int count;

        public Pair(int num, int count) {
            this.count = count;
            this.num = num;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        if (k == 0) return new int[0];

        Map<Integer, Integer> numCount = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            numCount.put(nums[i], numCount.getOrDefault(nums[i], 0) + 1);
        }

        ArrayList<Pair> numCountPair = new ArrayList<>();
        for (Integer num:numCount.keySet()) {
            Pair pair = new Pair(num, numCount.get(num));
            numCountPair.add(pair);
        }

        numCountPair.sort((o1, o2) -> -Integer.compare(o1.count, o2.count));
        int resSize = Math.min(numCountPair.size(), k);
        int[] res = new int[resSize];
        for (int i = 0; i < resSize; i++) {
            res[i] = numCountPair.get(i).num;
        }

        return res;
    }

    public static void main(String[] args) {
        int k = 2;
        int[] arr = {1,1,1,2,2,3,3,3,3};
        TopKFrequent topKFrequent = new TopKFrequent();
        int[] res = topKFrequent.topKFrequent(arr, k);

        System.out.println("Top k are: ");
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + ", ");
        }
    }
}
