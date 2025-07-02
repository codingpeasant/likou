# https://github.com/insideofdrop/Dropbox-Interview-Prep/blob/main/code/TokenBucket.java

import threading
import time
import random


class TokenBucket:
    def __init__(self, max_capacity, fill_rate):
        self.MAX_CAPACITY = max_capacity
        self.FILL_RATE = fill_rate
        self.bucket = []
        self.last_fill_timestamp = time.time()

        self.cond = threading.Condition()

    def fill(self):
        with self.cond:
            if len(self.bucket) == self.MAX_CAPACITY:
                print("Bucket is filled now.")
                self.cond.wait()

            now = time.time()
            elapsed_seconds = now - self.last_fill_timestamp
            num_tokens_to_add = min(
                self.MAX_CAPACITY - len(self.bucket),
                int(elapsed_seconds) * self.FILL_RATE,
            )
            print(
                f"{threading.current_thread().name} - numberTokens = {num_tokens_to_add}"
            )
            self.last_fill_timestamp = now

            for _ in range(num_tokens_to_add):
                self.bucket.append(random.randint(1, 100))

            if self.bucket:
                self.cond.notify_all()

    def get(self, n):
        if n <= 0:
            raise ValueError("Cannot get zero or negative number of tokens.")
        if n > self.MAX_CAPACITY:
            raise ValueError("Cannot get more tokens than max capacity.")

        result = []
        token_acquired = 0

        while token_acquired < n:
            with self.cond:
                while len(self.bucket) < 1:
                    print(f"{threading.current_thread().name} waiting to get more")
                    self.cond.wait()
                result.append(self.bucket.pop())
                token_acquired += 1
                self.cond.notify_all()

        return result


tb = TokenBucket(10, 2)
results = []


def get_worker(n, thread_name):
    tokens = tb.get(n)
    print(f"{thread_name} got tokens: {tokens}")
    with tb.cond:
        results.append((thread_name, tokens))


getThreads = []
for i in range(5):
    getThread = threading.Thread(
        target=get_worker, args=(2, f"get thread {i}"), name=f"get thread {i}"
    )
    getThreads.append(getThread)
    getThread.start()

fillThreads = []
for i in range(10):
    fillThread = threading.Thread(target=tb.fill, name=f"fill thread {i}")
    fillThreads.append(fillThread)
    fillThread.start()
    time.sleep(2)


for t in getThreads:
    t.join()
    with tb.cond:
        tb.cond.notify_all()

# Collect results
if results:
    for thread_name, tokens in results:
        print(f"Result from {thread_name}: {tokens}")
