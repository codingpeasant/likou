package DataStructure;

import java.util.*;

// https://leetcode.com/problems/task-scheduler/
// greedy
public class TaskScheduler {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskCounts = new HashMap<>();
        Queue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>(
                (a, b) -> a.getValue() != b.getValue() ? b.getValue() - a.getValue() : a.getKey() - b.getKey());
        for (char task : tasks) {
            taskCounts.put(task, taskCounts.getOrDefault(task, 0) + 1);
        }
        maxHeap.addAll(taskCounts.entrySet());

        int count = 0;
        while (!maxHeap.isEmpty()) {
            int countDown = n + 1;
            List<Map.Entry<Character, Integer>> tasksToReturn = new ArrayList<>();
            while (countDown > 0 && !maxHeap.isEmpty()) {
                Map.Entry<Character, Integer> cur = maxHeap.poll();
                cur.setValue(cur.getValue() - 1);
                if (cur.getValue() > 0) {
                    tasksToReturn.add(cur);
                }
                countDown--;
                count++;
            }

            maxHeap.addAll(tasksToReturn);

            if (maxHeap.isEmpty()) break; // if there is nothing left to execute, just break here
            count = count + countDown; // if countDown > 0, then it means we need to be idle
        }
        return count;
    }

    public static void main(String[] args) {
        TaskScheduler t = new TaskScheduler();
        char[] tasks = {'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'};
        System.out.println(t.leastInterval(tasks, 2));
    }

}
