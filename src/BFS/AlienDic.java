package BFS;

import java.util.*;

// https://leetcode.ca/2016-08-25-269-Alien-Dictionary/
public class AlienDic {
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    public String alienOrder(String[] words) {
        // Write your code here
        if (words == null || words.length == 0) {
            return "";
        }

        // step 1: construct the graph
        Map<Character, List<Character>> adjMap = new HashMap<>();
        constructGraph(words, adjMap);

        int numNodes = adjMap.size();

        StringBuilder result = new StringBuilder();

        // topological sorting
        Map<Character, Integer> indegreeMap = new HashMap<>();
        for (Character node : adjMap.keySet()) {
            indegreeMap.put(node, 0);
        }

        for (Character node : adjMap.keySet()) {
            for (Character neighbor : adjMap.get(node)) {
                indegreeMap.put(neighbor, indegreeMap.get(neighbor) + 1);
            }
        }

        // start from indegree=0
        Queue<Character> queue = new LinkedList<>();
        for (Character node : indegreeMap.keySet()) {
            if (indegreeMap.get(node) == 0) {
                // starting node, can only be one, cannot be 2 starting with 0 indegree; otherwise not a DAG and return ""
                queue.offer(node);
            }
        }

        while (!queue.isEmpty()) {
            char curNode = queue.poll();
            result.append(curNode);

            for (char neighbor : adjMap.get(curNode)) {
                int indegree = indegreeMap.get(neighbor);
                indegree -= 1;
                // indegreeMap.put(neighbor, indegreeMap.get(neighbor));

                // @note: key is here.
                // for A->B, B->C, A->C: C will not be counted until its indgree is 0

                if (indegree == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        if (result.length() < numNodes) {
            return "";
        }

        return result.toString();
    }

    private void constructGraph(String[] words, Map<Character, List<Character>> adjMap) {
        // construct nodes
        for (String word : words) {
            for (Character c : word.toCharArray()) {
                adjMap.put(c, new ArrayList<>()); // c to all its next
            }
        }

        // construct edges
        for (int i = 1; i < words.length; i++) {
            String prev = words[i - 1]; // compare the adjacent 2 words
            String curr = words[i];

            for (int j = 0; j < prev.length() && j < curr.length(); j++) {
                if (prev.charAt(j) != curr.charAt(j)) {
                    adjMap.get(prev.charAt(j)).add(curr.charAt(j));
                    break;
                }
            }
        }
    }

    public static void main(String args[]) {
        String[] words = new String[] {
                "wrt",
                "wrf",
                "er",
                "ett",
                "rftt"
        };

        AlienDic a = new AlienDic();
        System.out.println(a.alienOrder(words));
    }
}
