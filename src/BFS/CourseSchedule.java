package BFS;

import java.util.*;

// https://leetcode.com/problems/course-schedule
public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 0 || prerequisites.length == 0) return true;

        // Convert graph presentation from edges to indegree of adjacent list.
        int indegree[] = new int[numCourses];

        for (int i = 0; i < prerequisites.length; i++) // Indegree - how many prerequisites are needed.
            indegree[prerequisites[i][0]]++;

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                queue.add(i);
        }

        // How many courses don't need prerequisites.
        int canFinishCount = queue.size();
        while (!queue.isEmpty()) {
            int prerequisite = queue.remove(); // Already finished this prerequisite course.
            for (int i = 0; i < prerequisites.length; i++) {
                if (prerequisites[i][1] == prerequisite) {
                    indegree[prerequisites[i][0]]--;
                    if (indegree[prerequisites[i][0]] == 0) {
                        canFinishCount++;
                        queue.add(prerequisites[i][0]);
                    }
                }
            }
        }

        return (canFinishCount == numCourses);
    }

    // this times out in leetcode
    public boolean canFinishDFS(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap();
        for (int i = 0; i < numCourses; i++) {
            graph.putIfAbsent(i, new ArrayList<>());
        }

        for (int i = 0; i < prerequisites.length; i++) {
            graph.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        boolean[] visited = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }

        return true;
    }

    private boolean dfs(Map<Integer, List<Integer>> graph, boolean[] visited, int course) {
        if (visited[course]) {
            return false;
        }
        visited[course] = true;

        for (Integer adj : graph.get(course)) {
            if (!dfs(graph, visited, adj)) {
                return false;
            }
        }
        visited[course] = false;
        return true;
    }

    public static void main(String[] args) {
        CourseSchedule c = new CourseSchedule();
        int[][] prerequisites = {
                {3, 0},
                {3, 1},
                {3, 2},
                {1, 0},
                {2, 1},
                {0, 3}
        };
        System.out.println(c.canFinish(4, prerequisites));
        System.out.println(c.canFinishDFS(4, prerequisites));
    }
}
