package Other;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// https://leetcode.ca/2016-09-21-296-Best-Meeting-Point/
public class BestMeetingPoint {
    public int minTotalDistance(int[][] grid) {

        // empty, null check
        List<Integer> ipos = new ArrayList<>();
        List<Integer> jpos = new ArrayList<>();

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    ipos.add(i); // i is sorted in nature
                    jpos.add(j);
                }
            }
        }

        int sum = 0;
        // median is the min to all the nodes
        int iMid = ipos.get(ipos.size() / 2); // find the median i
        for(Integer pos : ipos){
            sum += Math.abs(pos - iMid);
        }

        Collections.sort(jpos); // sort j
        int jMid = jpos.get(jpos.size() / 2); // find the median of j
        for(Integer pos : jpos){
            sum += Math.abs(pos - jMid);
        }
        // i + j
        return sum;
    }

    public static void main(String[] args) {
        BestMeetingPoint out = new BestMeetingPoint();
        System.out.println(out.minTotalDistance(new int[][] { {1,0,0,0,1},{0,0,0,0,0},{0,0,1,0,0} }));
    }
}
