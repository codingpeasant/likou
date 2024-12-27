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
    HashMap<Integer, LinkedHashSet<Integer>> freqToKey;

    int capacity;

    // Initialize the frequency of data occurrences
    int min = -1;

    public LFUCache(int cap) {
        capacity = cap;
        vals = new HashMap<>();
        counts = new HashMap<>();
        freqToKey = new HashMap<>();
    }

    public int get(int key) {
        if (!vals.containsKey(key))
            return -1;

        int count = counts.get(key);
        counts.put(key, count + 1);
        freqToKey.get(count).remove(key);

        // Determine whether min should add 1
        if (count == min && freqToKey.get(count).size() == 0) {
            min++;
        }

        if (!freqToKey.containsKey(count + 1)) {
            freqToKey.put(count + 1, new LinkedHashSet<>());
        }

        freqToKey.get(count + 1).add(key);
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
            int minFreKey = freqToKey.get(min).iterator().next(); // first element in the set is the oldest
            freqToKey.get(min).remove(minFreKey);
            vals.remove(minFreKey);
            counts.remove(minFreKey);
        }

        vals.put(key, value);
        counts.put(key, 1);
        min = 1;
        if (!freqToKey.containsKey(1)) {
            freqToKey.put(1, new LinkedHashSet<>());
        }
        freqToKey.get(1).add(key);
    }
}

