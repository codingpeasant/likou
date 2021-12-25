package BFS;

import java.util.*;

// https://leetcode.com/problems/is-graph-bipartite/
public class IsGraphBipartite {
    public boolean isBipartite(int[][] graph) {
        Map<Integer, List<Integer>> graphMap = new HashMap<>();

        for (int i = 0; i < graph.length; i++) {
            graphMap.put(i, new ArrayList<>());
        }

        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++)
                graphMap.get(i).add(graph[i][j]);
        }

        for (int i = 0; i < graph.length; i++) {
            if (!bfs(graphMap, i)) {
                return false;
            }
        }

        return true;
    }

    private boolean bfs(Map<Integer, List<Integer>> graph, int start) {
        int[] color = new int[graph.size()]; // -1 white; 1 black; 0 null
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        color[start] = -1;

        while (!queue.isEmpty()) {
            Integer node = queue.poll();
            for (Integer adj : graph.get(node)) {
                if (color[adj] != 0) {
                    if (color[adj] != -color[node]) {
                        return false;
                    }
                } else {
                    color[adj] = -color[node];
                    queue.add(adj);
                }
            }
        }

        return true;
    }

    public boolean isBipartite1(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];

        for (int i = 0; i < n; i++) {              //This graph might be a disconnected graph. So check each unvisited node.
            if (colors[i] == 0 && !dfs(graph, colors, 1, i)) {
                return false;
            }
        }
        return true;
    }

    public boolean dfs(int[][] graph, int[] colors, int color, int node) {
        if (colors[node] != 0) {
            return color == colors[node];
        }
        colors[node] = color;
        for (int i = 0; i < graph[node].length; i++) {
            if (!dfs(graph, colors, -color, graph[node][i])) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        IsGraphBipartite c = new IsGraphBipartite();
        int[][] prerequisites = {
                {1, 2, 3},
                {0, 2},
                {0, 1, 3},
                {0, 2}
        };
        System.out.println(c.isBipartite(prerequisites));
        System.out.println(c.isBipartite1(prerequisites));
    }
}
