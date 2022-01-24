package JavaTest.threadpool;

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadPoolMain {
    public static void main(String[] args) throws Exception {
        ThreadPool threadPool = new ThreadPool(4);
        AtomicInteger atomicInteger = new AtomicInteger(0);

        for (int i = 0; i < 16; i++) {
            int taskNo = i;
            threadPool.execute(() -> {
                String message = Thread.currentThread().getName() + ": Task " + taskNo;
                try {
                    System.out.println(message + " started...");
                    Thread.sleep(500);
                    atomicInteger.addAndGet(1); // have to be atomic
                    System.out.println(message + " finished...");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
        }

        System.out.println(Thread.currentThread().getName() + " is waiting before stopping the thread poll...");
        Thread.sleep(5000);
        System.out.println(Thread.currentThread().getName() + " shutting down the thread pool...");
        threadPool.stop();
        System.out.println("The final value of the integer: " + atomicInteger.get());

        ExecutorService executor = Executors.newFixedThreadPool(5);
        List<Callable<Integer>> callables = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            Callable<Integer> worker = () -> {
                System.out.println("Runnable");
                try {
                    Thread.sleep(500);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                return new Random().nextInt(100);
            };
            callables.add(worker);
        }
        List<Future<Integer>> res = executor.invokeAll(callables);
        res.forEach(r -> {
            try {
                System.out.println(r.get());
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        });

        executor.shutdown();
        while (!executor.isTerminated());
        System.out.println("Finished all threads");
    }
}
