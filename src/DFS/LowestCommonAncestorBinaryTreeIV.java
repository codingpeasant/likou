package DFS;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// https://leetcode.ca/2020-07-02-1676-Lowest-Common-Ancestor-of-a-Binary-Tree-IV/
public class LowestCommonAncestorBinaryTreeIV {
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

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        if (root == null || nodes == null || nodes.length == 0)
            return null;
        Set<TreeNode> set = new HashSet<>(Arrays.asList(nodes));
        return depthFirstSearch(root, set);
    }

    public TreeNode depthFirstSearch(TreeNode root, Set<TreeNode> set) {
        if (root == null || set.contains(root))
            return root;
        TreeNode left = depthFirstSearch(root.left, set);
        TreeNode right = depthFirstSearch(root.right, set);
        if (left != null && right != null)
            return root;
        if (left != null)
            return left;
        if (right != null)
            return right;
        return null;
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

        System.out.println("LCA is: " + lowestCommonAncestor(node1, new TreeNode[]{node4, node6}).val);
    }

    public static void main(String[] args) {
        LowestCommonAncestorBinaryTreeII r = new LowestCommonAncestorBinaryTreeII();
        r.initialize();
    }
}
