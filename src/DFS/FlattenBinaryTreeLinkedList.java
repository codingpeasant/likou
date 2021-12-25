package DFS;

// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
public class FlattenBinaryTreeLinkedList {
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

    TreeNode prev = null;

    public void flatten(TreeNode root) {
        if (root == null) return;

        // post order from right to left and root the last
        flatten(root.right);
        flatten(root.left);

        root.left = null;
        root.right = prev;
        prev = root;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        flatten(node1);
        while (node1 != null) {
            System.out.print(node1.val + " -> ");
            node1 = node1.right;
        }
    }

    public static void main(String[] args) {
        FlattenBinaryTreeLinkedList mdt = new FlattenBinaryTreeLinkedList();
        mdt.initialize();
    }
}
