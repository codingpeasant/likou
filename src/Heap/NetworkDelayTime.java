package Heap;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

// https://leetcode.com/problems/network-delay-time/
public class NetworkDelayTime {
    public int networkDelayTime(int[][] times, int n, int k) {
        // convert to: source -> [dest, distance]
        Map<Integer, Map<Integer,Integer>> map = new HashMap<>();
        for(int[] time : times){
            map.putIfAbsent(time[0], new HashMap<>());
            map.get(time[0]).put(time[1], time[2]);
        }

        // distance, node into pq: int[0] is distance from source to dest, int[1] is dest
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        pq.add(new int[]{0, k});
        boolean[] visited = new boolean[n+1];
        int res = 0;

        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            int curNode = cur[1];
            int curDist = cur[0];
            if(visited[curNode]) continue;
            visited[curNode] = true;
            res = curDist;
            n--;
            if(map.containsKey(curNode)){
                for(int adjacent : map.get(curNode).keySet()){
                    pq.add(new int[]{curDist + map.get(curNode).get(adjacent), adjacent});
                }
            }
        }

        return n == 0 ? res : -1;
    }

    public static void main(String[] args) {
        NetworkDelayTime n = new NetworkDelayTime();
        int[][] times = new int[4][4];
        times[0][0] = 2;
        times[0][1] = 1;
        times[0][2] = 1;
        times[1][0] = 2;
        times[1][1] = 3;
        times[1][2] = 4;
        times[2][0] = 3;
        times[2][1] = 4;
        times[2][2] = 9;

        System.out.println(n.networkDelayTime(times, 4, 2));
    }
}
