package Concurrency;

// https://leetcode.com/problems/building-h2o/
public class BuildingH2O {

    private int hydrogenCount;
    private int oxygenCount;
    private int n = 0;
    private final int N = 10;

    public BuildingH2O() {
        hydrogenCount = 0;
        oxygenCount = 0;
    }

    public synchronized void hydrogen() throws InterruptedException {
        while (hydrogenCount == 2 && oxygenCount == 0) {
            wait();
        }
        hydrogenCount++;
        System.out.print('H');
        if (hydrogenCount == 2 && oxygenCount == 1) {
            hydrogenCount = oxygenCount = 0;
            n++;
            System.out.print('\n');
            notifyAll();
        }
    }

    public synchronized void oxygen() throws InterruptedException {
        while (hydrogenCount < 2 && oxygenCount == 1) {
            wait();
        }
        oxygenCount++;
        System.out.print('O');
        if (hydrogenCount == 2 && oxygenCount == 1) {
            hydrogenCount = oxygenCount = 0;
            n++;
            System.out.print('\n');
            notifyAll();
        }
    }

    public static void main(String[] args) {
        BuildingH2O b = new BuildingH2O();

        Thread t1 = new Thread(() -> {
            try {
                while (b.n < b.N)
                    b.oxygen();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread t2 = new Thread(() -> {
            try {
                while (b.n < b.N)
                    b.hydrogen();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        t1.start();
        t2.start();
    }
}
