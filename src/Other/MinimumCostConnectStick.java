package Other;

import java.util.PriorityQueue;

public class MinimumCostConnectStick {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int i = 0; i < sticks.length; i++) {
            minHeap.add(sticks[i]);
        }

        int cost = 0;
        while (minHeap.size() > 1) {
            int min = minHeap.poll();
            int secondMin = minHeap.poll();

            cost += min + secondMin;
            minHeap.add(min + secondMin);
        }

        return cost;
    }

    public static void main(String[] args) {
        MinimumCostConnectStick m = new MinimumCostConnectStick();
        int[] input = {4,2,3,1};
        System.out.println("Min cost: " + m.connectSticks(input));
    }
}
