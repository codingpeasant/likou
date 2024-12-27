package Binary;

import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeMap;

// https://leetcode.com/problems/most-beautiful-item-for-each-query/
public class MostBeautifulItemEachQuery {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        int[] result = new int[queries.length];
        Arrays.sort(items, Comparator.comparingInt(a -> a[0]));

        TreeMap<Integer, Integer> map = new TreeMap<>();
        map.put(0,0);
        int currMax = 0;
        for (int[] item : items) {
            currMax = Math.max(currMax, item[1]);      //maintain the largest beauty so far
            map.put(item[0], currMax);                 //store in treeMap
        }

        for (int i = 0; i < queries.length; ++i)
            result[i] = map.get(map.floorKey(queries[i]));

        return result;
    }

    public static void main(String[] args) {
        MostBeautifulItemEachQuery m = new MostBeautifulItemEachQuery();
        int[][] input = {
                {1,2},
                {3,2},
                {2,4},
                {5,6},
                {3,5}
        };
        int[] queries = {1,2,3,4,5,6};
        System.out.println(Arrays.toString(m.maximumBeauty(input, queries)));
    }
}
