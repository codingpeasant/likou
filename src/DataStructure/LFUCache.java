package DataStructure;

import java.util.HashMap;
import java.util.LinkedHashSet;

// https://leetcode.com/problems/lfu-cache/

public class LFUCache {
    // Save the key, value
    HashMap<Integer, Integer> vals;

    // Save the key to the value of the number of visits
    HashMap<Integer, Integer> counts;

    // 频率和一个里面所有key都是当前频率的list之间的映射
    HashMap<Integer, LinkedHashSet<Integer>> lists;

    int capacity;

    // Initialize the frequency of data occurrences
    int min = -1;

    public LFUCache(int cap) {
        capacity = cap;
        vals = new HashMap<>();
        counts = new HashMap<>();
        lists = new HashMap<>();
    }

    public int get(int key) {
        if (!vals.containsKey(key))
            return -1;

        int count = counts.get(key);
        counts.put(key, count + 1);
        lists.get(count).remove(key);

        // Determine whether min should add 1
        if (count == min && lists.get(count).size() == 0) {
            min++;
        }

        if (!lists.containsKey(count + 1)) {
            lists.put(count + 1, new LinkedHashSet<>());
        }

        lists.get(count + 1).add(key);
        return vals.get(key);
    }

    public void put(int key, int value) {
        if (capacity <= 0)
            return;

        if (vals.containsKey(key)) {
            vals.put(key, value);
            get(key);
            return;
        }

        if (vals.size() >= capacity) {
            int minFreKey = lists.get(min).iterator().next(); // first element in the set is the oldest
            lists.get(min).remove(minFreKey);
            vals.remove(minFreKey);
            counts.remove(minFreKey);
        }

        vals.put(key, value);
        counts.put(key, 1);
        min = 1;
        if (!lists.containsKey(1)) {
            lists.put(1, new LinkedHashSet<>());
        }
        lists.get(1).add(key);
    }
}

