package DFS;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.ca/2016-10-18-323-Number-of-Connected-Components-in-an-Undirected-Graph/
public class NumberOfConnectedComponents {
    boolean[] visited;

    private void connectedComponents(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            if (!visited[i]) {
                DFS(matrix, i);
            }
        }
    }

    private void DFS(int[][] matrix, int i) {
        visited[i] = true;
        System.out.print(i + " ");
        for (int j = 0; j < matrix.length; j++) {
            if (matrix[i][j] == 1 && !visited[j]) {
                DFS(matrix, j);
            }
        }
        System.out.print("\n");
    }


    public int countComponents(int n, int[][] edges) {
        int count = 0;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int[] visited = new int[n];
        for (int i = 0; i < graph.size(); i++) {
            if (visited[i] != 1) {
                count++;
                dfs(graph, visited, i);
            }
        }

        return count;
    }

    private void dfs(Map<Integer, List<Integer>> graph, int[] visited, int cur) {
        if (visited[cur] == 1) return;
        visited[cur] = 1;
        for (Integer adj : graph.get(cur)) {
            if (visited[adj] != 1)
                dfs(graph, visited, adj);
        }
    }

    // Driver method
    public static void main(String[] args) {
        int M[][] = new int[][]{
                {0, 1, 0, 0, 0},
                {1, 0, 0, 0, 0},
                {0, 0, 0, 1, 0},
                {0, 0, 1, 0, 1},
                {0, 0, 0, 1, 0},
        };
        NumberOfConnectedComponents N = new NumberOfConnectedComponents();
        N.visited = new boolean[M.length];
        System.out.println("Connected components are: ");
        N.connectedComponents(M);

        int[][] input = new int[][]{
                {0, 1},
                {1, 2},
                {3, 4}
        };

        System.out.println(N.countComponents(5, input));
    }
}
