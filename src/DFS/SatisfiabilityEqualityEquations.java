package DFS;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/satisfiability-of-equality-equations/
public class SatisfiabilityEqualityEquations {
    public boolean equationsPossible(String[] equations) {
        Map<Character, List<Character>> graph = new HashMap<>();
        List<char[]> notEqual = new ArrayList<>();

        for (String equation:equations) {
            char node1 = equation.charAt(0);
            char node2 = equation.charAt(3);

            if (equation.charAt(1) == '!') {
                notEqual.add(new char[]{node1, node2});
            } else {
                graph.putIfAbsent(node1, new ArrayList<>());
                graph.get(node1).add(node2);

                graph.putIfAbsent(node2, new ArrayList<>());
                graph.get(node2).add(node1);
            }
        }


        for (char[] nodePair : notEqual) {
            if (isConflict(nodePair[1], nodePair[0], graph, new boolean[26])) {
                return false;
            }
        }

        return true;
    }

    private boolean isConflict(char node2, char cur, Map<Character, List<Character>> graph, boolean[] visited) {
        if (cur == node2) {
            return true;
        }
        visited[cur - 'a'] = true;
        if (graph.get(cur) != null) {
            for (char adj : graph.get(cur)) {
                if (!visited[adj - 'a']) {
                    if (isConflict(node2, adj, graph, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        SatisfiabilityEqualityEquations s = new SatisfiabilityEqualityEquations();
        String[] equations = new String[] {
                "e!=c","b!=b","b!=a","e==d"
        };

        System.out.println(s.equationsPossible(equations));
    }
}
