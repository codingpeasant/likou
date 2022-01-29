package Concurrency;

// https://leetcode.com/problems/print-zero-even-odd/
public class PrintZeroEvenOdd {
    private int n;
    private int cur = 1;

    private boolean zeroPrinted = false;

    public PrintZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void zero() throws InterruptedException {
        while (cur <= n) {
            if (!zeroPrinted) {
                System.out.print(0);
                zeroPrinted = true;
                notifyAll();
            } else {
                wait();
            }
        }
    }

    public synchronized void even() throws InterruptedException {
        while (cur <= n) {
            if (zeroPrinted && cur % 2 == 0) {
                System.out.print(cur++);
                zeroPrinted = false;
                notifyAll();
            } else {
                wait();
            }
        }
    }

    public synchronized void odd() throws InterruptedException {
        while (cur <= n) {
            if (zeroPrinted && cur % 2 != 0) {
                System.out.print(cur++);
                zeroPrinted = false;
                notifyAll();
            } else {
                wait();
            }
        }

    }

    public static void main(String[] args) {
        PrintZeroEvenOdd p = new PrintZeroEvenOdd(5);

        Thread t1 = new Thread(() -> {
            try {
                p.zero();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread t2 = new Thread(() -> {
            try {
                p.even();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread t3 = new Thread(() -> {
            try {
                p.odd();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        t1.start();
        t2.start();
        t3.start();
    }
}
