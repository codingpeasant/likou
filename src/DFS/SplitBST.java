package DFS;

// https://leetcode.ca/2018-01-14-776-Split-BST/
public class SplitBST {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    // how to understand this? Suppose V = -1 which is smaller than any value in the BST, then res[0] = null res[1] = BST...
    public TreeNode[] splitBST(TreeNode root, int V) {
        TreeNode[] res = new TreeNode[]{null, null};
        if (root == null) {
            return res;
        }
        if (root.val <= V) { // the break point must be at right subtree
            res = splitBST(root.right, V);
            root.right = res[0]; // set right of the original root to the smaller on the left of its subtree
            res[0] = root;
        } else {
            res = splitBST(root.left, V);
            root.left = res[1]; // set left of the original root to the bigger on the right of its subtree
            res[1] = root;
        }
        return res;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(4);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(6);
        TreeNode node4 = new TreeNode(1);
        TreeNode node5 = new TreeNode(3);
        TreeNode node6 = new TreeNode(5);
        TreeNode node7 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;

        node2.left = node4;
        node2.right = node5;

        node3.left = node6;
        node3.right = node7;

        TreeNode[] twoTrees = splitBST(node1, 2);
        preOrder(twoTrees[0]);
        System.out.println();
        preOrder(twoTrees[1]);
    }

    public void preOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        System.out.print(node.val + ", ");
        preOrder(node.left);
        preOrder(node.right);
    }

    public static void main(String[] args) {
        SplitBST s = new SplitBST();
        s.initialize();
    }
}
