package DataStructure;

import java.util.*;

// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
public class InsertDeleteGetRandomDuplicates {
    ArrayList<Integer> nums;
    HashMap<Integer, Set<Integer>> locs;
    Random rand = new Random();

    /**
     * Initialize your data structure here.
     */
    public InsertDeleteGetRandomDuplicates() {
        nums = new ArrayList<>();
        locs = new HashMap<>();
    }

    /**
     * Inserts a value to the set. Returns true if the set did not already contain the specified element.
     */
    public boolean insert(int val) {
        boolean contain = locs.containsKey(val);
        if (!contain) locs.put(val, new HashSet<>()); // unique position of the same value
        locs.get(val).add(nums.size());
        nums.add(val);
        return !contain;
    }

    /**
     * Removes a value from the set. Returns true if the set contained the specified element.
     */
    public boolean remove(int val) {
        boolean contain = locs.containsKey(val);
        if (!contain) return false;
        int loc = locs.get(val).iterator().next(); // get the first location
        locs.get(val).remove(loc);
        if (loc < nums.size() - 1) {
            int lastone = nums.get(nums.size() - 1);
            nums.set(loc, lastone);
            locs.get(lastone).remove(nums.size() - 1);
            locs.get(lastone).add(loc);
        }
        nums.remove(nums.size() - 1);
        if (locs.get(val).isEmpty()) locs.remove(val); // val doesn't exist in nums anymore
        return true;
    }

    /**
     * Get a random element from the set.
     */
    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }

    public static void main(String[] arg) {
        InsertDeleteGetRandomDuplicates i = new InsertDeleteGetRandomDuplicates();
        i.insert(1);
        i.insert(2);
        i.insert(1);
        System.out.println(i.getRandom());
    }
}
