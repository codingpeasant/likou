package Other;

import java.util.LinkedList;

public class MovingAverage {
    double sum;
    int size;
    LinkedList<Integer> list;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.list = new LinkedList<>();
        this.size = size;
    }

    public double next(int val) {
        sum += val;
        list.offer(val);

        if(list.size()<=size){
            return sum/list.size();
        }

        sum -= list.poll();

        return sum/size;
    }

    public static void main(String[] args) {
        MovingAverage m = new MovingAverage(3);
        System.out.println(m.next(1));
        System.out.println(m.next(2));
        System.out.println(m.next(3));
        System.out.println(m.next(4));
        System.out.println(m.next(5));
    }
}
