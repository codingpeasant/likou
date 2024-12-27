package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/fruit-into-baskets/
public class FruitIntoBaskets {
    public int totalFruit(int[] tree) {
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        int i = 0, j;
        for (j = 0; j < tree.length; ++j) {
            count.put(tree[j], count.getOrDefault(tree[j], 0) + 1);
            while (count.size() > 2) {
                count.put(tree[i], count.get(tree[i]) - 1);
                count.remove(tree[i++], 0);
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }

    public static void main(String[] args) {
        FruitIntoBaskets f = new FruitIntoBaskets();
        int[] input = {3,3,3,1,2,1,1,2,3,3,4};
        System.out.println("Max fruits: " + f.totalFruit(input));
    }
}
