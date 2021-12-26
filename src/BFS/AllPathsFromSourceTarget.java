package BFS;

import java.util.*;

// https://leetcode.com/problems/all-paths-from-source-to-target/
public class AllPathsFromSourceTarget {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) { // BFS
        int target = graph.length - 1;
        List<List<Integer>> res = new ArrayList<>();
        Queue<List<Integer>> q = new LinkedList<>(); // store path like 0 -> 1 -> 4
        q.add(Collections.singletonList(0));

        while (!q.isEmpty()) {
            List<Integer> curPath = q.poll();

            if (curPath.get(curPath.size() - 1) == target) { // last element in the current path
                res.add(curPath);
                continue;
            }

            for (Integer node: graph[curPath.get(curPath.size() - 1)]) {
                List<Integer> curPathCopy = new ArrayList<>(curPath); // curPath is immutable collection due to List.of(0)
                curPathCopy.add(node);
                q.add(curPathCopy);
            }
        }

        return res;
    }

    public List<List<Integer>> allPathsSourceTarget2(int[][] graph) {
        int target = graph.length - 1;
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        backtrack(graph, path, res, target);
        return res;
    }

    private void backtrack(int[][] graph, List<Integer> curPath, List<List<Integer>> res, int target) {
        if (curPath.get(curPath.size() - 1) == target) {
            res.add(new ArrayList<>(curPath));
            return;
        }

        for (int node : graph[curPath.get(curPath.size() - 1)]) {
            curPath.add(node);
            backtrack(graph, curPath, res, target);
            curPath.remove(curPath.size() - 1);
        }
    }

    public static void main(String[] args) {
        int[][] graph = new int[][]{
                {4,3,1},
                {3,2,4},
                {3},
                {4},
                {}
        };
        AllPathsFromSourceTarget a = new AllPathsFromSourceTarget();
        List<List<Integer>> allPaths = a.allPathsSourceTarget(graph);
        for (List<Integer> allPath : allPaths) {
            System.out.println(allPath);
        }

        List<List<Integer>> allPaths2 = a.allPathsSourceTarget2(graph);
        for (List<Integer> allPath : allPaths2) {
            System.out.println(allPath);
        }
    }
}
