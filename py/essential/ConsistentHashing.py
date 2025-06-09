import bisect
import hashlib


class ConsistentHash:
    """
    A simple consistent hashing implementation that supports adding and removing nodes.

    Uses a sorted list of hash values (ring) to distribute keys across nodes.
    """
    import bisect
    import hashlib

    def __init__(self, nodes=None, replicas=100):
        """
        Initialize the consistent hash ring.

        :param nodes: initial list of node identifiers
        :param replicas: number of replicas for each node on the ring
        """
        self.replicas = replicas
        self.ring = []        # sorted list of hash values
        self._hash2node = {}  # map from hash value to node identifier
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key: str) -> int:
        """
        Generate a hash for a given key using md5 and return an integer.
        """
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        """
        Add a node to the hash ring with the given number of replicas.
        """
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            self.ring.insert(bisect.bisect(self.ring, h), h)
            self._hash2node[h] = node

    def remove_node(self, node: str) -> None:
        """
        Remove a node and its replicas from the hash ring.
        """
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            h = self._hash(replica_key)
            idx = bisect.bisect_left(self.ring, h)
            if idx < len(self.ring) and self.ring[idx] == h:
                self.ring.pop(idx)
                del self._hash2node[h]

    def get_node(self, key: str) -> str:
        """
        Given a key, return the closest node in the ring.
        """
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self._hash2node[self.ring[idx]]

# Example Usage
if __name__ == "__main__":
    ch = ConsistentHash(nodes=["node1", "node2", "node3"])
    print(ch.get_node("my_key"))
    ch.add_node("node4")
    print(ch.get_node("my_key"))
    ch.remove_node("node2")
    print(ch.get_node("my_key"))
