package Other;

public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;

        int insertPos = 0;
        for (int num: nums) {
            if (num != 0) nums[insertPos++] = num;
        }

        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }

    public static void main(String[] args) {
        MoveZeroes m = new MoveZeroes();
        int[] input = {0,1,0,3,12};
        m.moveZeroes(input);
        for (int num: input) {
            System.out.print(num + ", ");
        }

    }
}
