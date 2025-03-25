# https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind


class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node: Node, createdNodes: dict[int, Node]):
        if node is None:
            return None

        newNode = Node(node.val)
        createdNodes[node.val] = newNode

        for adjNode in node.neighbors:
            if (
                adjNode.val not in createdNodes
            ):  # create the clone of adjNode and add the adj of adjNode in the next iteration
                newNode.neighbors.append(self.dfs(adjNode, createdNodes))
            else:  # directly add the cloned node
                newNode.neighbors.append(createdNodes[adjNode.val])

        return newNode

    def cloneGraph(self, node: "Node") -> "Node":
        return self.dfs(node, {})


s = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node4.neighbors.append(node1)
node4.neighbors.append(node3)
print(s.cloneGraph(node1).val)
