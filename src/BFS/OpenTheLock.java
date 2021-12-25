package BFS;

import java.util.*;

// https://leetcode.com/problems/open-the-lock/
public class OpenTheLock {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));

        Queue<String> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        q.add("0000");
        visited.add("0000");

        int step = 0;
        // bfs
        while (!q.isEmpty()) {
            int count = q.size();
            for (int j = 0; j < count; j++) {
                String current = q.poll();
                if (current.equals(target)) {
                    return step;
                }

                if (deadSet.contains(current)) {
                    continue;
                }
                // for the 4 pads
                for (int i = 0; i < 4; i++) {
                    String up = addOne(current, i);
                    if (!visited.contains(up)) {
                        q.add(up);
                        visited.add(up);
                    }

                    String down = minusOne(current, i);
                    if (!visited.contains(down)) {
                        q.add(down);
                        visited.add(down);
                    }
                }
            }
            step++; // one step == on level of the possibility tree
        }

        return -1;
    }

    private String addOne(String state, int position) {
        char[] charArray = state.toCharArray();
        if (charArray[position] == '9') {
            charArray[position] = '0';
        } else {
            charArray[position] += 1;
        }

        return new String(charArray);
    }

    private String minusOne(String state, int position) {
        char[] charArray = state.toCharArray();
        if (charArray[position] == '0') {
            charArray[position] = '9';
        } else {
            charArray[position] -= 1;
        }

        return new String(charArray);
    }

    public static void main(String[] args) {
        OpenTheLock o = new OpenTheLock();
        System.out.println("Min turns: " + o.openLock(new String[]{"0201","0101","0102","1212","2002"}, "0202"));
    }
}
