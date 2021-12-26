package Other;

// https://leetcode.com/problems/jump-game-ii/
public class JumpGame2 {
    // greedy
    public int jump(int[] A) {
        int jumps = 0, curEnd = 0, curFarthest = 0;
        for (int i = 0; i < A.length - 1; i++) {
            curFarthest = Math.max(curFarthest, i + A[i]);
            if (i == curEnd) { // Once the current point reaches curEnd, then trigger another jump
                jumps++;
                curEnd = curFarthest;
            }
        }
        return jumps;
    }

    // can also use bfs
    public static void main(String[] args) {
        JumpGame2 j = new JumpGame2();
        int[] nums = {2,3,1,1,4};
        System.out.println(j.jump(nums));
    }
}
