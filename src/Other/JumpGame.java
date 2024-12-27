package Other;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/jump-game/
// greedy
public class JumpGame {
    public boolean canJump(int[] A) {
        int max = 0;
        for (int i = 0; i < A.length; i++) {
            if (i > max) {
                return false;
            }
            max = Math.max(A[i] + i, max);
        }
        return true;
    }

    // Time Limit Exceeded
    public boolean bfs(int[] A) {
        Queue<Integer> bfsQueue = new LinkedList<>();
        bfsQueue.add(0);
        while (!bfsQueue.isEmpty()) {
            int curIndex = bfsQueue.poll();

            for (int i = 0; i <= A[curIndex]; i++) {
                if (curIndex + i >= A.length - 1) {
                    return true;
                }
                bfsQueue.add(curIndex + i);
            }
        }

        return false;
    }

    public static void main(String args[]) {
        JumpGame j = new JumpGame();
        int[] input = {1, 1, 2, 3, 0, 1};
        System.out.println("Can reach last index: " + j.canJump(input));
        System.out.println("Can reach last index (bfs): " + j.bfs(input));
    }
}
