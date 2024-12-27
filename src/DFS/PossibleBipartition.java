package DFS;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/possible-bipartition/
public class PossibleBipartition {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        int[] colors = new int[n];

        Map<Integer, List<Integer>> graphMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            graphMap.put(i, new ArrayList<>());
        }

        for (int[] dislike : dislikes) {
            graphMap.get(dislike[0] - 1).add(dislike[1] - 1);
            graphMap.get(dislike[1] - 1).add(dislike[0] - 1);
        }

        for (int i = 0; i < n; i++) {              //This graph might be a disconnected graph. So check each unvisited node.
            if (colors[i] == 0 && !dfs(graphMap, colors, 1, i)) {
                return false;
            }
        }
        return true;
    }

    public boolean dfs(Map<Integer, List<Integer>> graph, int[] colors, int color, int node) {
        if (colors[node] != 0) {
            return color == colors[node];
        }
        colors[node] = color;
        for (Integer next : graph.get(node)) {
            if (!dfs(graph, colors, -color, next)) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        PossibleBipartition p = new PossibleBipartition();
        int n = 4;
        int[][] dislikes = new int[][]{
                {1, 2},
                {1, 3},
                {2, 4}
        };

        System.out.println(p.possibleBipartition(n, dislikes));
    }
}
