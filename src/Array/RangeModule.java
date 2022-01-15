package Array;

import java.util.Map;
import java.util.TreeMap;

// https://leetcode.com/problems/range-module/
// extension of InsertInterval
public class RangeModule {
    TreeMap<Integer, Integer> first = new TreeMap<>(); // left:right

    public RangeModule() {
    }

    public void addRange(int left, int right) {
        while (true) {
            // Try to merge with existing ones.
            Map.Entry<Integer, Integer> entry = first.floorEntry(right);
            if (entry == null || entry.getValue() < left) // null means the interval to add is on the left
                break;
            left = Math.min(left, entry.getKey());
            right = Math.max(right, entry.getValue());
            first.remove(entry.getKey());
        }
        first.put(left, right);
    }

    public boolean queryRange(int left, int right) {
        Map.Entry<Integer, Integer> entry = first.floorEntry(left);
        return entry != null && entry.getValue() >= right; // the entry can include [left,right)
    }

    public void removeRange(int left, int right) {
        // Add the range first, to make the code simpler.
        addRange(left, right);
        Map.Entry<Integer, Integer> entry = first.floorEntry(left);
        first.remove(entry.getKey());
        if (entry.getKey() < left)
            first.put(entry.getKey(), left);
        if (entry.getValue() > right)
            first.put(right, entry.getValue());
    }

    public static void main(String[] args) {
        RangeModule r = new RangeModule();
        r.addRange(10,20);
        r.addRange(15,25);
        r.removeRange(14,16);
        System.out.println(r.queryRange(13,15));
        System.out.println(r.queryRange(16,17));
    }

}
