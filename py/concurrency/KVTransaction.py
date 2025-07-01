# Dropbox

# KV store。
# begin()
# read(transactionId, key)
# write(transactionId, value)
# commit(transactionId)
# 要设法保证每个transaction都是atomic的。就是要求实现一个in memory的map支持transaction，begin返回一个transactionID, 实现put(transacId, k, v) get(transactId, k)以及commit，需要考虑多个transaction交错的情况以及abort


from collections import defaultdict
import random
import uuid
import threading


class Transaction:
    def __init__(self):
        self.pendingWrites = defaultdict(str)  # key → value
        self.active = True


class TransactionalKVStore:
    def __init__(self):
        self.store = defaultdict(tuple)  # key → (value, version)
        self.txs = defaultdict(Transaction)  # txId → Transaction
        self.tx_snapshots = defaultdict(
            lambda: defaultdict(int)
        )  # txId → {key: version}
        self.key_locks = defaultdict(threading.Lock)  # per-key locks
        self.global_lock = threading.Lock()

    def begin(self):
        txId = str(uuid.uuid4())
        self.txs[txId] = Transaction()
        with self.global_lock:
            # Snapshot current key versions
            snapshot = {k: v[1] for k, v in self.store.items()}
        self.tx_snapshots[txId] = snapshot
        return txId

    def put(self, txId, key, value):
        tx = self._get_tx(txId)
        tx.pendingWrites[key] = value

    def get(self, key):
        # Dirty read prevention: only see committed store
        with self.key_locks[key]:
            return self.store.get(key, None)

    def commit(self, txId):
        tx = self._get_tx(txId)
        keys = sorted(tx.pendingWrites.keys())
        snapshot = self.tx_snapshots[txId]
        acquired = []

        try:
            # Acquire key locks
            for key in keys:
                lock = self.key_locks[key]
                lock.acquire()
                acquired.append(lock)

            # Check for optimistic lock conflicts
            for key in keys:
                committed_version = self.store.get(key, (None, 0))[1]
                snap_version = snapshot.get(key, 0)
                if committed_version != snap_version:
                    raise Exception(f"Optimistic lock failed: key '{key}' was modified (expected version {snap_version}, got {committed_version})")

            # Apply writes
            for key, value in tx.pendingWrites.items():
                self.store[key] = (value, committed_version+1)


            print(f"{threading.current_thread().name} - committed")

        finally:
            # Clean up
            tx.active = False
            del self.txs[txId]
            del self.tx_snapshots[txId]
            for lock in reversed(acquired):
                lock.release()

    def abort(self, txId):
        tx = self._get_tx(txId)
        with self.global_lock:
            tx.active = False
            del self.txs[txId]

    def _get_tx(self, txId):
        tx = self.txs.get(txId)
        if not tx or not tx.active:
            raise Exception(f"Transaction {txId} is invalid or aborted.")
        return tx


store = TransactionalKVStore()

def reader():
    key = random.randint(0, 9)
    value = store.get(key)
    print(f"{threading.current_thread().name} - {key}:{value}")

def writer():
    txId = store.begin()
    for _ in range(5):
        key = random.randint(0, 9)
        store.put(txId, key, str(random.randint(100, 300)))
    store.commit(txId)

readerThreads = []
writerThreads = []
for i in range(10):
    writerThread = threading.Thread(target=writer, name=f"writer-{i}")
    writerThreads.append(writerThread)
    writerThread.start()

for i in range(10):
    readerThread = threading.Thread(target=reader, name=f"reader-{i}")
    readerThreads.append(readerThread)
    readerThread.start()



# txId = store.begin()
# store.put(txId, "key1", "value1")
# store.put(txId, "key1", "value2")
# store.commit(txId)
# print(store.get("key1"))
# txId = store.begin()
# store.put(txId, "key1", "value3")
# store.put(txId, "key1", "value4")
# store.abort(txId)
# print(store.get("key1"))
