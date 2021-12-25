package Heap;

import java.util.*;

// https://leetcode.com/problems/path-with-maximum-probability/
public class PathMaximumProbability {
    public double maxProbability1(int n, int[][] edges, double[] succProb, int start, int end) {
        Map<Integer, Map<Integer, Double>> graph = new HashMap<>();

        for (int i = 0; i < edges.length; i++) {
            int[] pair = edges[i];
            graph.putIfAbsent(pair[0], new HashMap<>());
            graph.get(pair[0]).put(pair[1], succProb[i]);
            graph.putIfAbsent(pair[1], new HashMap<>());
            graph.get(pair[1]).put(pair[0], succProb[i]);
        }

        double[] probability = new double[n];
        probability[start] = 1;
        boolean[] visited = new boolean[n];
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.comparingDouble(i -> -probability[i]));
        minHeap.add(start);

        while (!minHeap.isEmpty()) {
            int current = minHeap.poll();
            if (current == end) {
                return probability[current];
            }
            if (visited[current]) continue;
            visited[current] = true;
            for (int adj:graph.getOrDefault(current, new HashMap<>()).keySet()) {
                double newPro = probability[current] * graph.get(current).get(adj);
                probability[adj] = Math.max(probability[adj], newPro);
                minHeap.add(adj);
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] edges = {
                {0,1},
                {1,2},
                {0,2}
        };

        double[] succProb = {0.5, 0.5, 0.3};
        int start = 0;
        int end = 2;

        PathMaximumProbability p = new PathMaximumProbability();
        System.out.println(p.maxProbability1(n, edges, succProb, start, end));
    }
}
