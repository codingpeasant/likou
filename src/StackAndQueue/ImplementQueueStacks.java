package StackAndQueue;

import java.util.Stack;

// https://leetcode.com/problems/implement-queue-using-stacks/
public class ImplementQueueStacks {
    final private Stack<Integer> myQueue;

    public ImplementQueueStacks() {
        myQueue = new Stack<>();
    }

    public void push(int x) {
        Stack<Integer> temp = new Stack<>();
        while (!myQueue.empty()) {
            temp.push(myQueue.pop());
        }
        myQueue.push(x);
        while (!temp.empty()) {
            myQueue.push(temp.pop());
        }
    }

    public int pop() {
        return this.myQueue.pop();
    }

    public int peek() {
        return this.myQueue.peek();
    }

    public boolean empty() {
        return this.myQueue.empty();
    }

    public static void main(String[] args) {
        ImplementQueueStacks i = new ImplementQueueStacks();
        i.push(1);
        i.push(2);
        i.push(3);
        i.push(4);
        System.out.println(i.peek());
        i.pop();
        System.out.println(i.peek());
    }

}
