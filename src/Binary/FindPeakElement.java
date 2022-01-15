package Binary;

// https://leetcode.com/problems/find-peak-element/
// Consider that each local maximum is one valid peak.
public class FindPeakElement {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        FindPeakElement f = new FindPeakElement();
        int[] input = {1,2,1,3,5,6,4};
        System.out.println("peak is " + f.findPeakElement(input));
    }
}
