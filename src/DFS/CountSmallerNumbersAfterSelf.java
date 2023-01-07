package DFS;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/count-of-smaller-numbers-after-self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
public class CountSmallerNumbersAfterSelf {
    int[] count;

    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<>();

        count = new int[nums.length];
        int[] indices = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            indices[i] = i;
        }
        mergesort(nums, indices, 0, nums.length - 1);
        for (int i = 0; i < count.length; i++) {
            res.add(count[i]);
        }
        return res;
    }

    private void mergesort(int[] nums, int[] indexes, int start, int end) {
        if (end <= start) {
            return;
        }
        int mid = (start + end) / 2;
        mergesort(nums, indexes, start, mid);
        mergesort(nums, indexes, mid + 1, end);

        merge(nums, indexes, start, end);
    }

    private void merge(int[] nums, int[] indexes, int start, int end) {
        int mid = (start + end) / 2;
        int leftIndex = start;
        int rightIndex = mid + 1;
        int smallerElementOnRightCount = 0;
        int[] newIndexes = new int[end - start + 1];

        int sortedIndex = 0;
        while (leftIndex <= mid && rightIndex <= end) {
            if (nums[indexes[rightIndex]] < nums[indexes[leftIndex]]) {
                newIndexes[sortedIndex] = indexes[rightIndex];
                smallerElementOnRightCount++;
                rightIndex++;
            } else {
                newIndexes[sortedIndex] = indexes[leftIndex];
                count[indexes[leftIndex]] += smallerElementOnRightCount;
                leftIndex++;
            }
            sortedIndex++;
        }
        while (leftIndex <= mid) {
            newIndexes[sortedIndex] = indexes[leftIndex];
            count[indexes[leftIndex]] += smallerElementOnRightCount;
            leftIndex++;
            sortedIndex++;
        }
        while (rightIndex <= end) {
            newIndexes[sortedIndex++] = indexes[rightIndex++];
        }
        for (int i = start; i <= end; i++) {
            indexes[i] = newIndexes[i - start];
        }
    }

    public static void main(String[] args) {
        CountSmallerNumbersAfterSelf c = new CountSmallerNumbersAfterSelf();
        System.out.println(c.countSmaller(new int[]{5,2,6,1}));
    }
}
