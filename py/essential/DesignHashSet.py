# https://leetcode.com/problems/design-hashset/description/
# Neet

class MyHashSet:
    def __init__(self):
        self.size = 10
        self.buckets = [[] for _ in range(self.size)]

    # Adds key to a bucket
    def add(self, key):
        bucket = self._getBucket(key)
        if not self.contains(key):
            bucket.append(key)

    # Removes key from bucket
    def remove(self, key):
        bucket = self._getBucket(key)
        if self.contains(key):
            bucket.remove(key)

    # Returns true if buckets contain key
    def contains(self, key):
        bucket = self._getBucket(key)
        return key in bucket

    # Returns the bucket corresponding to the key
    def _getBucket(self, key):
        hash = self._getHash(key)
        return self.buckets[hash]

    # Trivial hash function
    def _getHash(self, key):
        return key % self.size


hashSet = MyHashSet()
print(hashSet.add(1))
print(hashSet.add(10))
print(hashSet.contains(1))
print(hashSet.remove(1))
print(hashSet.contains(1))
