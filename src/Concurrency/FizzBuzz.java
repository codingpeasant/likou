package Concurrency;

// https://leetcode.com/problems/fizz-buzz-multithreaded/
public class FizzBuzz {
    private int n;
    private int cur = 1;

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz.run() outputs "fizz".
    public synchronized void fizz() throws InterruptedException {
        while (cur <= n) {
            if (cur % 3 == 0  && cur % 5 != 0) {
                System.out.print("fizz");
                cur++;
                notifyAll();
            } else {
                wait();
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public synchronized void buzz() throws InterruptedException {
        while (cur <= n) {
            if (cur % 3 != 0  && cur % 5 == 0) {
                System.out.print(" buzz ");
                cur++;
                notifyAll();
            } else {
                wait();
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public synchronized void fizzbuzz() throws InterruptedException {
        while (cur <= n) {
            if (cur % 3 == 0 && cur % 5 == 0) {
                System.out.print(" fizzbuzz ");
                cur++;
                notifyAll();
            } else {
                wait();
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void number() throws InterruptedException {
        while (cur <= n) {
            if (cur % 3 != 0 && cur % 5 != 0) {
                System.out.print(" " + cur++ + " ");
                notifyAll();
            } else {
                wait();
            }
        }
    }

    public static void main(String[] args) {
        FizzBuzz f = new FizzBuzz(15);

        Thread one = new Thread(() -> {
            try {
                f.fizz();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread two = new Thread(() -> {
            try {
                f.buzz();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread three = new Thread(() -> {
            try {
                f.fizzbuzz();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread four = new Thread(() -> {
            try {
                f.number();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        two.start();
        three.start();
        one.start();
        four.start();
    }

}
