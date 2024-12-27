package JavaTest.threadpool;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadPool {
    private final List<PoolWorker> workerThreads;
    private final BlockingQueue<Runnable> queue;

    public ThreadPool(int nThreads) {
        queue = new LinkedBlockingQueue<>();
        workerThreads = new ArrayList<>();

        for (int i = 0; i < nThreads; i++) {
            PoolWorker worker = new PoolWorker();
            workerThreads.add(worker);
            new Thread(worker).start();
        }
    }

    public void execute(Runnable task) {
        queue.add(task);
    }

    public void stop() {
        for (PoolWorker worker : workerThreads) {
            worker.doStop();
        }
    }

    private class PoolWorker implements Runnable {
        boolean isStopped = false;

        public void run() {
            Runnable task;

            while (!isStopped) {
                try {
                    task = queue.poll(1, TimeUnit.SECONDS);
                    if (task != null)
                        task.run();
                    else
                        System.out.println(Thread.currentThread().getName() + " is waiting for more tasks...");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            if (!queue.isEmpty()) {
                List<Runnable> leftTasks = new ArrayList<>();
                queue.drainTo(leftTasks);
                System.out.println(Thread.currentThread().getName() + " finishing " + leftTasks.size() + " last tasks...");
                for (Runnable leftTask : leftTasks) {
                    leftTask.run();
                }
            }
            System.out.println(Thread.currentThread().getName() + " shutting down...");
        }

        public void doStop() {
            isStopped = true;
        }
    }
}