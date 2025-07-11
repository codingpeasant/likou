# https://massivealgorithms.blogspot.com/2016/03/dropbox-interview-misc.html

import threading
from time import sleep


class ReadWriteLock:
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.write_requests = 0
        self.condition = threading.Condition()

    def lock_read(self):
        with self.condition:
            while self.writers > 0 or self.write_requests > 0:
                print(f"{threading.current_thread().name} - lock_read wait")
                self.condition.wait()
            self.readers += 1
            print(f"{threading.current_thread().name} - lock_read done")

    def unlock_read(self):
        with self.condition:
            self.readers -= 1
            self.condition.notify_all()
            print(f"{threading.current_thread().name} - unlock_read done")

    def lock_write(self):
        with self.condition:
            self.write_requests += 1
            while self.readers > 0 or self.writers > 0:
                print(f"{threading.current_thread().name} - lock_write wait")
                self.condition.wait()
            self.write_requests -= 1
            self.writers += 1
            print(f"{threading.current_thread().name} - lock_write done")

    def unlock_write(self):
        with self.condition:
            self.writers -= 1
            self.condition.notify_all()
            print(f"{threading.current_thread().name} - unlock_write done")


def writeWorker(rwl: ReadWriteLock):
    rwl.lock_write()
    sleep(1)
    rwl.unlock_write()


def readWorker(rwl: ReadWriteLock):
    rwl.lock_read()
    sleep(1)
    rwl.unlock_read()


rwl = ReadWriteLock()

fillThreads = []
for i in range(5):
    fillThread = threading.Thread(
        target=writeWorker, args=(rwl,), name=f"write thread {i}"
    )
    fillThreads.append(fillThread)
    fillThread.start()

getThreads = []
for i in range(5):
    getThread = threading.Thread(
        target=readWorker, args=(rwl,), name=f"read thread {i}"
    )
    getThreads.append(getThread)
    getThread.start()

for getThread in getThreads:
    getThread.join()

for fillThread in fillThreads:
    fillThread.join()
