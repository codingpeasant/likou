package Array;

import java.util.PriorityQueue;

// https://leetcode.com/problems/car-fleet/
// go from the larger position to smaller, see if the previous car could catch up
public class CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (int i = 0; i < position.length; i++) {
            pq.offer(new int[]{i, position[i]});
        }
        double time = 0;
        int count = 0;
        while (!pq.isEmpty()) {
            int[] next = pq.poll();
            int index = next[0];
            int pos = next[1];
            int spd = speed[index];
            double needTime = (double) (target - pos) / spd;
            if (needTime > time) { // this car cannot catch up with the one ahead, forming a fleet
                count++;
                time = needTime;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        CarFleet c = new CarFleet();
        int[] speed = {
                2, 4, 1, 1, 3
        };
        int[] pos = {
                10, 8, 0, 5, 3
        };
        System.out.println(c.carFleet(12, pos, speed));
    }

}
