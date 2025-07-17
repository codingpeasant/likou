import bisect
from collections import defaultdict
import hashlib


class ConsistentHash:
    """
    Consistent hashing without replicas.
    Supports adding/removing nodes and moving impacted keys.
    """

    def __init__(self, nodes=None):
        self.ring = []  # sorted list of node hashes
        self._hash2node = {}  # hash -> node id
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node: str, keys=None):
        """
        Add a node to the ring and return keys that should move to it.
        :param node: node id
        :param keys: list of keys to check for movement (optional)
        :return: list of (key, new_node) for keys that move to this node
        """
        h = self._hash(node)
        idx = bisect.bisect_right(self.ring, h)
        print("add node index", idx)
        self.ring.insert(idx, h)
        print("ring", self.ring)
        self._hash2node[h] = node

        moved = []
        if keys:
            for key in keys:
                new_node = self.get_node(key)
                if new_node == node:
                    moved.append((key, node))
        return moved

    def remove_node(self, node: str, keys=None):
        """
        Remove a node from the ring and return keys that should move away from it.
        :param node: node id
        :param keys: list of keys to check for movement (optional)
        :return: list of (key, new_node) for keys that move away from this node
        """
        h = self._hash(node)
        idx = bisect.bisect_left(self.ring, h)
        if idx < len(self.ring) and self.ring[idx] == h:
            self.ring.pop(idx)
            del self._hash2node[h]

        moved = []
        if keys:
            for key in keys:
                old_node = node
                new_node = self.get_node(key)
                if old_node != new_node:
                    moved.append((key, new_node))
        return moved

    def get_node(self, key: str) -> str:
        """
        Given a key, return the node responsible for it.
        """
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        print(self.ring)
        if idx == len(self.ring):
            idx = 0
        return self._hash2node[self.ring[idx]]


class ConsistentHash1:
    def __init__(self):
        self.ring = []
        self.hashToNode = defaultdict(str)

    def getHash(self, input: str):
        return int(hashlib.md5(input.encode()).hexdigest(), 16)

    def addNode(self, nodeId: str):
        h = self.getHash(nodeId)
        idx = bisect.bisect_right(self.ring, h)
        self.ring.insert(idx, h)
        self.hashToNode[h] = nodeId

    def removeNode(self, nodeId: str):
        h = self.getHash(nodeId)
        idx = bisect.bisect_left(self.ring, h)
        if idx < len(self.ring) and self.ring[idx] == h:
            self.ring.pop(idx)
            self.hashToNode.pop(h)
        return self.hashToNode

    def getNode(self, key: str):
        if not self.ring:
            return None
        h = self.getHash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.hashToNode[self.ring[idx]]


# Example Usage
if __name__ == "__main__":
    ch = ConsistentHash1()
    for i in range(10):
        ch.addNode(f"node{i}")
    print(ch.removeNode(f"node1"))
    print(ch.removeNode("fffff"))
    for i in range(10):
        print(ch.getNode(str(i)))
