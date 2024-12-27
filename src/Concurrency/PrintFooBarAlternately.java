package Concurrency;

// https://leetcode.com/problems/print-foobar-alternately/
public class PrintFooBarAlternately {
    int n = 10;
    boolean fooPrinted = false;

    public synchronized void foo() throws InterruptedException {
        for (int i = 0; i < n; i++) {
            if (fooPrinted) wait();
            System.out.print("foo");
            fooPrinted = true;
            notifyAll();
        }
    }

    public synchronized void bar() throws InterruptedException {
        for (int i = 0; i < n; i++) {
            if (!fooPrinted) wait();
            System.out.println("bar");
            fooPrinted = false;
            notifyAll();
        }
    }

    public static void main(String[] args) {
        PrintFooBarAlternately p = new PrintFooBarAlternately();

        Thread t1 = new Thread(() -> {
            try {
                p.foo();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread t2 = new Thread(() -> {
            try {
                p.bar();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        t1.start();
        t2.start();

    }
}
