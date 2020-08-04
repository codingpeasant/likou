package SlidingWindow;

import java.util.HashMap;
import java.util.Map;

public class FruitIntoBasckets {
    public int totalFruit(int[] tree) {
        Map<Integer, Integer> count = new HashMap<>();
        int i = 0, j;
        for (j = 0; j < tree.length; ++j) {
            count.put(tree[j], count.getOrDefault(tree[j], 0) + 1);
            if (count.size() > 2) {
                count.put(tree[i], count.get(tree[i]) - 1);
                count.remove(tree[i++], 0);
            }
        }
        return j - i;
    }

    public static void main(String[] args) {
        FruitIntoBasckets f = new FruitIntoBasckets();
        int[] input = {3,3,3,1,2,1,1,2,3,3,4};
        System.out.println("Max fruits: " + f.totalFruit(input));
    }
}
