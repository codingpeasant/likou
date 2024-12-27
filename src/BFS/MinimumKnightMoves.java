package BFS;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

// https://leetcode.ca/2019-03-11-1197-Minimum-Knight-Moves/
public class MinimumKnightMoves {
    private final int[][] DIRECTIONS = new int[][] {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
    public int minKnightMoves(int x, int y) {
        // 四个象限方向步数是一样的
        x = Math.abs(x);
        y = Math.abs(y);

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});

        Set<String> visited = new HashSet<>();
        visited.add("0,0");

        int result = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                int curX = cur[0];
                int curY = cur[1];
                if (curX == x && curY == y) {
                    return result;
                }

                for (int[] d: DIRECTIONS) {
                    int newX = curX + d[0];
                    int newY = curY + d[1];
                    // If you remove this condition newX >= -1 && newY >= -1) this solution would give TLE.
                    if (!visited.contains(newX + "," + newY) && newX >= -1 && newY >= -1) {
                        queue.add(new int[] {newX, newY});
                        visited.add(newX + "," + newY);
                    }
                }
            }
            result++;
        }
        return -1;
    }
}
