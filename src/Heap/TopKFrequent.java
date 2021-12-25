package Heap;

import java.util.*;

// https://leetcode.com/problems/top-k-frequent-elements/
public class TopKFrequent {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap =
                new PriorityQueue<>((a, b) -> (b.getValue() - a.getValue()));
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            maxHeap.add(entry);
        }

        List<Integer> res = new ArrayList<>();
        while (res.size() < k) {
            Map.Entry<Integer, Integer> entry = maxHeap.poll();
            res.add(entry.getKey());
        }

        return res.stream().mapToInt(e -> e).toArray();
    }

    public static void main(String[] args) {
        int k = 2;
        int[] arr = {1, 1, 1, 2, 2, 3, 3, 3, 3};
        TopKFrequent topKFrequent = new TopKFrequent();
        int[] res = topKFrequent.topKFrequent(arr, k);

        System.out.println("Top k are: ");
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + ", ");
        }
    }
}
