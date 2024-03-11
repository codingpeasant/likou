class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getSampleTree():
    """
            1
          /   \      
         2     3
          \   /  \
           6 5    4   
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    node6 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.right = node5
    node3.right = node4
    node3.left = node6

    return node1


def getSampleBST():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node4.left = node2
    node2.left = node1
    node2.right = node3

    return node4


def getCompleteTree():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    return node1


def preOrder(root: TreeNode):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)
