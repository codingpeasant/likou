package Heap;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class FindKPairsSmallestSums {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) return res;
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a, b) -> a[0] + a[1] - (b[0] + b[1]));
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                pq.offer(new Integer[] {nums1[i], nums2[j]});
            }
        }
        for (int i = 0; i < k; i++) {
            if (!pq.isEmpty()) {
                Integer[] arr = pq.poll();
                List<Integer> list = new ArrayList<>(Arrays.asList(arr));
                res.add(list);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int k = 3;
        int[] arr1 = {1,2,2,3,3,3,3};
        int[] arr2 = {1,5,7,9,10};
        FindKPairsSmallestSums findKPairsSmallestSums = new FindKPairsSmallestSums();
        List<List<Integer>> res = findKPairsSmallestSums.kSmallestPairs(arr1, arr2, k);

        System.out.println("Top K smallest sum are: ");
        for (int i = 0; i < res.size(); i++) {
            for (int j = 0; j < res.get(i).size(); j++) {
                System.out.print(res.get(i).get(j) + ", ");
            }
            System.out.print("\n");
        }
    }
}
