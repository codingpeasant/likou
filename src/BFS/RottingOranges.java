package BFS;

import java.util.LinkedList;
import java.util.Queue;

public class RottingOranges {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int rows = grid.length;
        int cols = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();
        int countFresh = 0;
        // Put the position of all rotten oranges in queue
        // count the number of fresh oranges
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.add(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    countFresh++;
                }
            }
        }

        // if count of fresh oranges is zero --> return 0
        if (countFresh == 0) return 0;
        int minutes = 0;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // bfs starting from initially rotten orange
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] point = queue.poll();
                for (int[] direction : directions) {
                    int x = point[0] + direction[0];
                    int y = point[1] + direction[1];
                    //if x or y is out of bound
                    //or the orange at (x , y) is already rotten
                    //or the cell at (x , y) is empty
                    //we do nothing
                    if (x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] == 0 || grid[x][y] == 2)
                        continue;
                    //mark the orange at (x , y) as rotten
                    grid[x][y] = 2;
                    //put the new rotten orange at (x , y) in queue
                    queue.add(new int[]{x, y});
                    //decrease the count of fresh oranges by 1
                    countFresh--;
                }
            }
            minutes++;
        }
        return countFresh == 0 ? minutes - 1 : -1;
    }

    public static void main(String[] args) {
        RottingOranges r = new RottingOranges();
        int[][] input = {
                {2, 1, 1},
                {1, 1, 0},
                {0, 1, 1}
        };
        System.out.println("Minutes: " + r.orangesRotting(input));
    }
}
