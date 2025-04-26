# https://leetcode.com/problems/design-hashmap/description/
# Neet

class MyHashMap:

    def __init__(self):
        # better to be a prime number, less collision
        # store (key, value) in the bucket
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            bucket.append((key,value))
        else:
            bucket[index] = (key, value)

    def get(self, key: int) -> int:
        bucket, index = self.getIndex(key)
        if index < 0:
            return -1
        else:
            return bucket[index][1]

    def remove(self, key: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            return
        else:
            bucket.remove(bucket[index])
    
    def hashKey(self, key):
        return key % self.size
    
    # find the target bucket and index of the key
    # if index > 0, then (key, value) exist
    # if index < 0, then (key, value) not exist
    def getIndex(self, key):
        hashResult = self.hashKey(key)
        bucket = self.buckets[hashResult]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1
  
s=MyHashMap()
s.put(1, 1) # The map is now [[1,1]]
s.put(2, 2) # The map is now [[1,1],[2,2]]
print(s.get(1)) # return 1, the map is now [[1,1],[2,2]]
print(s.get(3)) # return -1 (not found), the map is now [[1,1],[2,2]]
s.put(2, 1) # update the existing value, the map is now [[1,1],[2,1]]
print(s.get(2)) # return 1, the map is now [[1,1],[2,1]]
s.remove(2) # remove the mapping for 2, the map is now [[1,1]]
print(s.get(2)) # return -1 (not found), the map is now [[1,1]]