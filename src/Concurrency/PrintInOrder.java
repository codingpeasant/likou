package Concurrency;

import java.util.concurrent.CountDownLatch;

// https://leetcode.com/problems/print-in-order/
public class PrintInOrder {
    CountDownLatch c1 = new CountDownLatch(1);
    CountDownLatch c2 = new CountDownLatch(1);

    public PrintInOrder() {

    }

    public void first() throws InterruptedException {
        System.out.println("first");
        c1.countDown();
    }

    public void second() throws InterruptedException {
        c1.await();
        System.out.println("second");
        c2.countDown();
    }

    public void third() throws InterruptedException {
        c2.await();
        System.out.println("third");
    }

    public static void main(String[] args) {
        PrintInOrder p = new PrintInOrder();

        Thread one = new Thread(() -> {
            try {
                p.first();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread two = new Thread(() -> {
            try {
                p.second();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread three = new Thread(() -> {
            try {
                p.third();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        two.start();
        three.start();
        one.start();
    }
}
