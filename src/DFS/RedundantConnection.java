package DFS;

import java.util.*;

// https://leetcode.com/problems/redundant-connection/
public class RedundantConnection {
    int[] parent, size;

    public int[] findRedundantConnection(int[][] edges) {
        parent = new int[edges.length];
        size = new int[edges.length];
        for (int i = 0; i < edges.length; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        for (int[] e : edges) {
            if (!union(e[0] - 1, e[1] - 1)) return new int[]{e[0], e[1]};
        }
        return new int[]{};
    }

    public int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]); // Path compression
    }

    public boolean union(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false; // Return False if u and v are already union
        if (size[pu] > size[pv]) { // Union by larger size
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return true;
    }

    public int[] findRedundantConnectionDFS(int[][] edges) {
        int n = edges.length;
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int[] edge : edges) {
            int node1 = edge[0], node2 = edge[1];
            if (dfs(adjList, node1, node2, 0)) {
                return edge;
            } else {
                adjList.putIfAbsent(node1, new ArrayList<>());
                adjList.get(node1).add(node2);
                adjList.putIfAbsent(node2, new ArrayList<>());
                adjList.get(node2).add(node1);
            }
        }
        return null;
    }

    public boolean dfs(Map<Integer, List<Integer>> adjList, int node1, int node2, int pre) {
        if (node1 == node2) return true;
        List<Integer> adjs = adjList.get(node1);
        if (adjs != null && !adjs.isEmpty()) {
            for (int adj : adjs) {
                if (adj == pre) continue;
                if (dfs(adjList, adj, node2, node1)) // cannot just return dfs(...) here
                    return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        RedundantConnection r = new RedundantConnection();
        int[][] input = {
                {1, 2},
                {2, 3},
                {3, 4},
                {1, 4},
                {1, 5}
        };
        System.out.println(Arrays.toString(r.findRedundantConnection(input)));
        System.out.println(Arrays.toString(r.findRedundantConnectionDFS(input)));
    }

}
