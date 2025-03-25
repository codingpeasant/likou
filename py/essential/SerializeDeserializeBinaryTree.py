# Blind
# Grind
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/?envType=problem-list-v2&envId=oizxjoit

from typing import List
from tree_node import *


class Codec:
    empty, splitter = "X", ","

    # preorder
    def serialize(self, root: TreeNode):
        def buildString(curNode: TreeNode, serializedStr: List[str]):
            if not curNode:
                serializedStr.append(Codec.empty)
                serializedStr.append(Codec.splitter)
            else:
                serializedStr.append(str(curNode.val))
                serializedStr.append(Codec.splitter)
                buildString(curNode.left, serializedStr)
                buildString(curNode.right, serializedStr)

        stringArr = []
        buildString(root, stringArr)
        return "".join(stringArr)

    def deserialize(self, data: str):
        splittedData = data.split(self.splitter)

        # preorder too
        def buildTree():
            val = splittedData.pop(0)
            if val == Codec.empty:
                return None
            else:
                parentNode = TreeNode(val)
                parentNode.left = buildTree()
                parentNode.right = buildTree()
                return parentNode

        if not data:
            return None
        else:
            return buildTree()


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
sampleTree = getSampleTree()
print(ser.serialize(sampleTree))
preOrder(deser.deserialize(ser.serialize(getSampleTree())))
