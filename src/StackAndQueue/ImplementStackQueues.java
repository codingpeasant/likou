package StackAndQueue;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/implement-stack-using-queues/
public class ImplementStackQueues {
    final private Queue<Integer> myStack;
    public ImplementStackQueues() {
        this.myStack = new LinkedList<>();
    }

    public void push(int x) {
        Queue<Integer> temp = new LinkedList<>();
        while (!myStack.isEmpty()) {
            temp.add(myStack.poll());
        }
        myStack.add(x);

        while (!temp.isEmpty()) {
            myStack.add(temp.poll());
        }
    }

    public int pop() {
        return this.myStack.poll();
    }

    public int top() {
        return this.myStack.peek();
    }

    public boolean empty() {
        return this.myStack.isEmpty();
    }

    public static void main(String[] args) {
        ImplementStackQueues i = new ImplementStackQueues();
        i.push(1);
        i.push(2);
        i.push(3);
        i.push(4);
        System.out.println(i.top());
        i.pop();
        System.out.println(i.top());
        i.push(5);
        System.out.println(i.top());
    }
}
