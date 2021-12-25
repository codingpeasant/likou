package DataStructure;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/count-good-meals/
// https://leetcode.com/problems/count-good-meals/discuss/999119/Java-HashMap-Two-Sum-O(N)
public class CountGoodMeal {
    int mod = 1000000007;
    public int countPairs(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        long res = 0;
        for (int num : arr) {
            int power = 1;
            for (int i = 0; i < 22; i++) {
                if (map.containsKey(power - num)) {
                    res += map.get(power - num);
                    res %= mod;
                }
                power *= 2;
            }
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        return (int) res;
    }

    public static void main(String args[]) {
        CountGoodMeal c = new CountGoodMeal();
        System.out.println(c.countPairs(new int[]{1,1,1,3,3,3,7}));
    }
}
