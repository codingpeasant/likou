package Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://leetcode.com/problems/interval-list-intersections/
public class IntervalListIntersections {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> res = new ArrayList();
        for (int i = 0, j = 0; i < firstList.length && j < secondList.length; ) {
            int start = Math.max(firstList[i][0], secondList[j][0]);
            int end = Math.min(firstList[i][1], secondList[j][1]);
            if (start <= end) // has overlapping
                res.add(new int[]{start, end});
            if (firstList[i][1] < secondList[j][1])
                ++i;
            else
                ++j;
        }
        return res.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        IntervalListIntersections i = new IntervalListIntersections();
        int[][] a = {
                {0,2},
                {5,10},
                {13,23},
                {24,25}
        };

        int[][] b = {
                {1,5},
                {8,12},
                {15,24},
                {25,26}
        };
        System.out.println(Arrays.deepToString(i.intervalIntersection(a, b)));
    }
}
