package Binary;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/range-frequency-queries/
public class RangeFrequencyQueries {
    Map<Integer, List<Integer>> freqMap = new HashMap<>();

    public RangeFrequencyQueries(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            freqMap.putIfAbsent(arr[i], new ArrayList<>());
            freqMap.get(arr[i]).add(i);
        }
    }

    public int query(int left, int right, int value) {
        List<Integer> valueIndices = freqMap.get(value);
        if (valueIndices == null) return 0;
        // binary search the ceil of left (or left itself) and the floor of right (or right itself)
        int leftCeil = findCeil(valueIndices, left);
        int rightFloor = findFloor(valueIndices, right);

        if (leftCeil == -1 || rightFloor == -1) return 0;
        return rightFloor - leftCeil + 1;
    }

    private int findCeil (List<Integer> valueIndices, int index) {
        int left = 0, right = valueIndices.size() -1;
        int ceil = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (valueIndices.get(mid) > index) {
                // if `x` is less than the middle element, the ceil exists in the
                // subarray nums[left…mid]; update ceil to the middle element
                // and reduce our search space to the left subarray nums[left…mid-1]
                ceil = mid;
                right = mid - 1;
            } else if (valueIndices.get(mid) < index) {
                // if `x` is more than the middle element, the ceil exists in the
                // right subarray nums[mid+1…right]
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return ceil;
    }

    private int findFloor (List<Integer> valueIndices, int index) {
        int left = 0, right = valueIndices.size() -1;
        int floor = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (valueIndices.get(mid) > index) {
                right = mid - 1;
            } else if (valueIndices.get(mid) < index) {
                floor = mid;
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return floor;
    }

    public static void main(String[] args) {
        int[] arr = {12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56};
        RangeFrequencyQueries rangeFrequencyQueries = new RangeFrequencyQueries(arr);
        System.out.println(rangeFrequencyQueries.query(1, 2, 4));
        System.out.println(rangeFrequencyQueries.query(11, 11, 33));
    }
}
