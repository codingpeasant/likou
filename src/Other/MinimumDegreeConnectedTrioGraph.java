package Other;

// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
import java.util.HashMap;
import java.util.Map;

public class MinimumDegreeConnectedTrioGraph {
    public int minTrioDegree(int n, int[][] edges) {
        int min = Integer.MAX_VALUE;
        Map<Integer, Integer> degrees = new HashMap<>(); // vertex, degree
        boolean[][] isEdge = new boolean[n + 1][n + 1];

        for (int[] edge : edges) {
            degrees.put(edge[0], degrees.getOrDefault(edge[0], 0) + 1);
            degrees.put(edge[1], degrees.getOrDefault(edge[1], 0) + 1);
            isEdge[edge[0]][edge[1]] = true;
            isEdge[edge[1]][edge[0]] = true;
        }

        for (int[] edge : edges) {
            for (int i = 1; i <= n; i++) {
                // suppose 1,2,3 is a trio, when i = 3, i should be connected to both sides of edge[1][2],
                // so isEdge[1][3] and isEdge[2][3] should be both true
                if (isEdge[i][edge[0]] && isEdge[i][edge[1]]) {
                    // subtract 6 because we do not count inner edges of a trio
                    int degree = degrees.get(i) + degrees.get(edge[0]) + degrees.get(edge[1]) - 6;
                    min = Math.min(min, degree);
                }
            }
        }

        if (min == Integer.MAX_VALUE)
            return -1;
        return min;
    }

    public static void main(String[] args) {
        MinimumDegreeConnectedTrioGraph m = new MinimumDegreeConnectedTrioGraph();
        int[][] graph = {
                {1,2},
                {1,3},
                {3,2},
                {4,1},
                {5,2},
                {3,6}
        };
        System.out.println(m.minTrioDegree(6, graph));
    }
}
