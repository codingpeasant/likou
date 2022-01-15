package Binary;

import java.util.*;

// https://leetcode.com/problems/range-frequency-queries/
public class RangeFrequencyQueries {
    Map<Integer, TreeMap<Integer, Integer>> map = new HashMap<>();
    public RangeFrequencyQueries(int[] arr) {
        for(int i = 0; i < arr.length;i++){
            map.putIfAbsent(arr[i], new TreeMap<>());
            map.get(arr[i]).put(i, map.get(arr[i]).size());
        }
    }

    public int query(int left, int right, int value) {
        if(!map.containsKey(value)) return 0;
        TreeMap<Integer, Integer> nums = map.get(value);
        Integer a = nums.ceilingKey(left), b = nums.floorKey(right);
        if(a == null || b == null) return 0;
        return nums.get(b) - nums.get(a) +1;
    }

    public static void main(String[] args) {
        int[] arr = {12, 33, 4, 56, 22, 33, 2, 34, 33, 22, 12, 33, 34, 56, 33};
        RangeFrequencyQueries rangeFrequencyQueries = new RangeFrequencyQueries(arr);
        System.out.println(rangeFrequencyQueries.query(1, 2, 4));
        System.out.println(rangeFrequencyQueries.query(11, 11, 33));
    }
}
