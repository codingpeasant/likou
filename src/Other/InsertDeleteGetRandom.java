package Other;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

// https://leetcode.com/problems/insert-delete-getrandom-o1/
public class InsertDeleteGetRandom {
    ArrayList<Integer> nums;
    HashMap<Integer, Integer> locs;
    Random rand = new Random();

    public InsertDeleteGetRandom() {
        nums = new ArrayList<>();
        locs = new HashMap<>();
    }

    public boolean insert(int val) {
        boolean contain = locs.containsKey(val);
        if ( contain ) return false;
        locs.put(val, nums.size());
        nums.add(val);
        return true;
    }

    public boolean remove(int val) {
        boolean contain = locs.containsKey(val);
        if (!contain) return false;
        int position = locs.get(val);
        if (nums.size() - 1 > position) {
            // if not the last element, put the last element at the current position
            int lastElement = nums.get(nums.size() - 1);
            nums.set(position, lastElement);
            locs.put(lastElement, position);

        }
        // remove last element
        nums.remove(nums.size() - 1);
        locs.remove(val);
        return true;
    }

    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }

    public static void main(String[] args) {
        InsertDeleteGetRandom i = new InsertDeleteGetRandom();
        i.insert(1);
        i.insert(2);
        i.insert(3);
        System.out.println(i.getRandom());
        i.remove(3);
        i.remove(1);
    }
}
