# https://leetcode.com/discuss/post/1367130/doordash-phone-interview-by-anonymous_us-vag4/
from collections import defaultdict


class Node:
    def __init__(self, key, value, isActive):
        self.key = key
        self.value = value
        self.isActive = isActive
        self.children: list[Node] = []

    def equals(self, node: "Node"):
        if node is None:
            return False

        return (
            self.key == node.key
            and self.value == node.value
            and self.isActive == node.isActive
        )


class Solution:
    def getChildNodes(self, root: Node):
        res = defaultdict(Node)
        if not root:
            return res
        for child in root.children:
            res[child.key] = child
        return res


    def getModifiedItems(self, oldMenuRoot: Node, newMenuRoot: Node):
        if not oldMenuRoot and not newMenuRoot:
            return 0

        count = 0
        if oldMenuRoot or newMenuRoot or not oldMenuRoot.equals(newMenuRoot):
            count += 1

        oldChildren = self.getChildNodes(oldMenuRoot)
        newChildren = self.getChildNodes(newMenuRoot)

        for oldChild in oldChildren:
            count += self.getModifiedItems(oldChildren.get(oldChild), newChildren.get(oldChild))
        
        for newChild in newChildren:
            count += self.getModifiedItems(oldChildren.get(newChild), newChildren.get(newChild))

        return count


s = Solution()
print(s.getModifiedItems(Node(1, 2, False), Node(1, 2, True)))
